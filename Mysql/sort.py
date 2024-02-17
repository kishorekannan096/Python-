from MySQL_Connection import initialize_connection

def getting_values() :
    connection = initialize_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM numbers"
    cursor.execute(query)
    rows = cursor.fetchall()
    listValues = []
    for row in rows:
        listValues.append(row[0])
    print("Table values: ", listValues)
    bubblesort(listValues)
    cursor.close()
    connection.close()

def bubblesort(values) :
    n = len(values)
    for i in range(n):
        for j in range(0, n-i-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
    print_sortedValues(values)

def print_sortedValues(values) :
    print("Sorted Array Values: ", *values)

getting_values()
