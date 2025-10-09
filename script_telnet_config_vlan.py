import asyncio
import getpass
import telnetlib3

HOST = "192.168.101.90"
user = input("Enter your remote account: ")
password = getpass.getpass()

async def main():
    reader, writer = await telnetlib3.open_connection(HOST)

    await reader.read_until(b"Username: ")
    writer.write(user.encode('ascii') + b"\n")
    
    if password:
        await reader.read_until(b"Password: ")
        writer.write(password.encode('ascii') + b"\n")

    await reader.read_until(b">")
    writer.write(b"conf t\n")

    for x in range(2, 9):  # VLANs de 2 a 8
        writer.write(b"vlan " + str(x).encode('ascii') + b"\n")
        writer.write(b"name Python_VLAN_" + str(x).encode('ascii') + b"\n")

    writer.write(b"end\n")
    writer.write(b"wr\n")
    writer.write(b"exit\n")

    data = await reader.read()
    print(data.decode('ascii'))

    writer.close()

asyncio.run(main())
