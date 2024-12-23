import asyncio

from asyncpg import connect

from loader import DB_URI


class DB_M:
    def __init__(self, db_uri):
        self.db_uri = db_uri


    async def execute(self, arg, *args):
        con = await connect(self.db_uri)
        
        await con.execute(arg, *args)

        await con.close()


    async def fetch(self, *args):
        con = await connect(self.db_uri)
        
        values = await con.fetch(*args)

        await con.close()

        return values
    

    async def fetchrow(self, *args):
        con = await connect(self.db_uri)
        
        value = await con.fetchrow(*args)

        await con.close()

        return value


    async def create_tables(self): 
        await self.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            username VARCHAR (64),
            first_name VARCHAR (64) NOT NULL,
            last_name VARCHAR (64),
            reg_time TIMESTAMP DEFAULT now(), 
            status_user VARCHAR (64) DEFAULT 'user'
            )
            '''
        )


    async def add_new_user(self, user_id, username, first_name, last_name):
        await self.execute(
            '''
            INSERT INTO users (user_id, username, first_name, last_name)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT DO NOTHING
            ''', 
            user_id, username, first_name, last_name
        )


    async def get_user_by_id(self, user_id):
        user = await self.fetchrow(
            '''
            SELECT *
              FROM users
             WHERE user_id = $1
            ''', 
            user_id
        )
        
        return user
    

    async def get_status_user(self, user_id):
        status_user = await db_manage.fetchrow(
            '''
            SELECT status_user
              FROM users
             WHERE user_id = $1
            ''',
            user_id
        )

        return status_user
    

    async def get_admins(self):
        admins = await db_manage.fetch(
            '''
            SELECT *
              FROM users
             WHERE status_user = 'main_admin' OR status_user = 'admin'
            '''
        )

        return admins


    async def update_user(self, user_id, username=None, first_name=None, last_name=None, status_user=None) -> None:
        old_user = await self.get_user_by_id(user_id)

        if username is None: 
            username = old_user[1]
        
        if first_name is None: 
            first_name = old_user[2]
        
        if last_name is None: 
            last_name = old_user[3]
        
        if status_user is None: 
            status_user = old_user[5]
        
        await db_manage.execute(
            '''
            UPDATE users 
              SET username = $1, first_name = $2, last_name = $3, status_user = $4
            WHERE user_id = $5
            ''',
            username, first_name, last_name, status_user, user_id
        )


    async def count_users(self) -> int:
        count = await db_manage.fetchrow(
            '''
            SELECT COUNT(1)
              FROM users
            '''
        )

        return count[0]
    

    async def get_users_id(self):
        users_id = await db_manage.fetch(
            '''
            SELECT user_id
              FROM users
            '''
        )

        return users_id
    



db_manage = DB_M(DB_URI)

# async def test():
#     users_id = await db_manage.get_users_id()
#     print(len(users_id))

# asyncio.run(test())