import OpenOPC #OpenOPC-DA
import csv
import datetime

# Configure OPC DA connection details
opc_server_name = "Kepware.KEPServerEX.V6"  # Replace with your OPC server name
opc_group_name = "teste"
opc_item_id = "Simulation Examples.Functions.Ramp1"  # Replace with the ID of the OPC item

# Create an OPC client
opc = OpenOPC.client()

try:
    # Connect to the OPC server
    opc.connect(opc_server=opc_server_name)

    print("Connected to OPC DA server:", opc_server_name)

    # Read the value from the OPC item
    value = opc.read(opc_item_id, opc_group_name)

    # Get the current timestamp
    timestamp = datetime.datetime.now()

    print(opc[opc_item_id])

    # Prepare data for CSV
    data = [timestamp.strftime("%Y-%m-%d %H:%M:%S"), str(value)]

    # Write data to CSV file
    with open('opc_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

    print("Data written to opc_data.csv")

finally:
    # Disconnect from the OPC server
    opc.close()