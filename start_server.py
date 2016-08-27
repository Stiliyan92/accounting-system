import settings as s
from server.receiver import LogReceiver

server = LogReceiver(s.SERVER, s.PORT, s.VIRT_HOST, s.ADMIN, s.ROUTING_KEY)
server.receive_logs()
