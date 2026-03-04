import paho.mqtt.client as mqtt
subscribe = "masukkan.kata"
def on_message(client, userdata, msg):
    data= str(msg.payload.decode())
    print("pesan diterima:", data)

client = mqtt.Client()
client.on_message = on_message

server = "mqtt-dashboard.com"
client.connect(server, 1883)
client.subscribe(subscribe)

print("menunggu pesan...")
client.loop_forever()