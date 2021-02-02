def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful.")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
    
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
        
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def init(hostname, username, userpassword):    
		connection = create_server_connection(hostname, username, userpassword)
		create_database(connection, "CREATE DATABASE playerdata")
		connection.close()
		connection = create_db_connection(hostname, username, userpassword, "playerdata")
		connection.close()
		
		create_database_query = """
		CREATE TABLE database (
			user_id INT PRIMARY KEY
			max_energy INT
			curr_energy INT
			salary_base INT
			salary_inc INT
			curr_balance INT
			stonks_count INT
			item_num VARCHAR(12)
			meme_num VARCHAR(8)
		);
		"""
		
		execute_query(connection, create_database_query)
		
def update_data(connection, user_id, max_energy, curr_energy, salary_base, salary_inc, curr_balance, stonks_count, item_list, meme_list):
		# item_list will be a string with 11 characters, 1 representing "have this item" and 0 representing "don't have this item"
		# meme_list is same as item_list
		replace_data_query = f"""
		REPLACE INTO database(user_id, max_energy, curr_energy, salary_base, salary_inc, curr_balance, stonks_count, item_num, meme_num)
		VALUES({user_id}, {max_energy}, {curr_energy}, {salar_base}, {salar_inc}, {curr_balance}, {stonks_count}, {item_list}, {meme_list});
		"""
		
		execute_query(connection, replace_data_query)
		connection.close()

def read_data(connection, user_id):
		get_data_query = f"""
		SELECT *
		FROM playerdata
		WHERE user_id = {user_id};
		"""
		
		cursor = connection.cursor()
    result = None
    try:
        cursor.execute(get_data_query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
        
    connection.close()
    
def update_energy(connection): # Update energy
		update_query = """
		UPDATE playerdata
		SET curr_energy = max_energy
		"""
		
		execute_query(connection, update_query)
