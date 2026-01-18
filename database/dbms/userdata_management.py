from . import supabase_connection as supabase


class UserDataManagement:

    def insert_user_data(self, user):

        with supabase.get_db_connection() as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(
                    """
                    INSERT INTO userdata (name, surname, age) 
                    VALUES (%s, %s, %s)
                    """,
                    (user.name, user.surname, user.age)
                )
                connection.commit()
                print("Insert successful!")

            except Exception as e:
                connection.rollback()
                print(f"Insert failed: {e}")

            finally:
                cursor.close()


    def get_user_data(self, user_id):

        with supabase.get_db_connection() as connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT * FROM userdata WHERE id = %s", (user_id,))
                row = cursor.fetchone()
                if row:
                    print(row)

            except Exception as e:
                connection.rollback()
                print(f"Get failed: {e}")

            finally:
                cursor.close()