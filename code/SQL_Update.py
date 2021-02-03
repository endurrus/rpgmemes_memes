def create_db_connection():
	host_name = ""
	user_name = ""
	db_name = ""
	user_password = ""
	connection = None
	try:
		connection = mysql.connector.connect(
			host=host_name,
			user=user_name,
			passwd=user_password,
			database=db_name
		)
		print("MySQL Database connection successful")
	except Exception as err:
		print(f"Error: '{err}'")
	
	return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Exception as err:
        print(f"Error: '{err}'")

def init():
	connection = create_db_connection()
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
		item_list VARCHAR(11)
		meme_list VARCHAR(7)
	);
	"""
	execute_query(connection, create_database_query)

def update_energy(): # Update energy
		update_query = """
		UPDATE database
		SET curr_energy = max_energy
		"""
		connection = create_db_connection()
		execute_query(connection, update_query)


def update_income(): # Update Income
		update_query = """
		UPDATE database
		SET salary_base += salary_inc
		"""
		connection = create_db_connection()
		execute_query(connection, update_query)		
		
def get_field(user_id, field_name): # Read Field
	get_data_query = f"""
		SELECT {field_name}
		FROM database
		WHERE user_id = {user_id};
	"""
	
	connection = create_db_connection()
	cursor = connection.cursor()
	result = None
	
	try:
		cursor.execute(get_data_query)
		result = cursor.fetchall()
		return result[0][0]
	except Exception as err:
		print(f"Error: '{err}'")
		
	connection.close()
	
def change_field(user_id, field_name, change): # Change Field
	if field_name == "item_list" or field_name == "meme_list":
		data = get_field(user_id, field_name)
		data = data[:change] + '1' + data[change+1:]
		change_query = f"""
			UPDATE database
			SET {field_name} = {data}
			WHERE user_id = {user_id}
		"""
		connection = create_db_connection()
		execute_query(connection, change_query)
		connection.close()
	
	else:
		change_query = f"""
			UPDATE database
			SET {field_name} += {change}
			WHERE user_id = {user_id}
		"""
		connection = create_db_connection()
		execute_query(connection, change_query)
		connection.close()
		
def check_user(user_id): #Check if a user exists
	check_query = f"""
	SELECT *
	FROM database
	WHERE user_id = {user_id}
	"""
	
	connection = create_db_connection()
	cursor = connection.cursor()
	result = None
	
	try:
		cursor.execute(get_data_query)
		result = cursor.fetchall()
		if len(result) == 0:
			return True
		else:
			return False
	except Exception as err:
		print(f"Error: '{err}'")
	
def init_user(user_id): # When a new user is created
	init_user_query = f"""
	    INSERT INTO database(user_id, max_energy, curr_energy, salary_base, salary_inc, curr_balance, stonks_count, item_num, meme_num)
		VALUES({user_id}, 100, {curr_energy}, 2400, 500, 0, 0, "00000000000", "0000000");
	"""
		
	connection = create_db_connection()
	execute_query(connection, init_user_query)
	connection.close()
