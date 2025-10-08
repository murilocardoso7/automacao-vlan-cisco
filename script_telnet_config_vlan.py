import asyncio
import getpass
import telnetlib3

HOST = "192.168.101.99"
user = input("Enter your remote account (press Enter if none): ")
password = getpass.getpass("Password: ")

async def main():
    reader, writer = await telnetlib3.open_connection(HOST, port=23)

    data = await reader.read(4096)

    # Detecta se há prompt de username
    if "Username" in data or "User" in data:
        writer.write(user + "\n")
        await asyncio.sleep(0.3)
        data = await reader.read(4096)

    # Detecta se há prompt de senha
    if "Password" in data:
        writer.write(password + "\n")
        await asyncio.sleep(0.3)
        data = await reader.read(4096)

    # Comandos Cisco
    cmds = [
        "enable",
        "conf t",
        "vlan 2",
        "name Python_VLAN_2",
        "vlan 3",
        "name Python_VLAN_3",
        "vlan 4",
        "name Python_VLAN_4",
        "vlan 5",
        "name Python_VLAN_5",
        "vlan 6",
        "name Python_VLAN_6",
        "vlan 7",
        "name Python_VLAN_7",
        "end",
        "show vlan brief",
        "exit"
    ]

    print("\n--- Executando comandos no roteador ---\n")

    for cmd in cmds:
        writer.write(cmd + "\n")
        await asyncio.sleep(0.5)
        output = await reader.read(4096)
        if output.strip():
            print(output.strip())

    writer.close()
    await writer.wait_closed()

asyncio.run(main())

