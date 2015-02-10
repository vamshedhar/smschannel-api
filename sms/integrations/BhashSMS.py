import requests

class BhashSMSIntegration():
  USERNAME = 'imgiitr'
  PASS = 'imgiitrsms'
  SENDER_ID = 'IMGSRE'

  PARAMS = {
    'user': USERNAME,
    'pass': PASS,
    'sender': SENDER_ID,,
    'priority': 'ndnd',
    'smstype': 'normal',
  }

  API_BASE_URL = {
    'MESSAGE': 'http://bhashsms.com/api/sendmsg.php',
    'DELIVERY_REPORT': 'http://bhashsms.com/api/recdlr.php',
  }

  class Meta:
    abstract = True

  def __init__(self, message):
    self.message = message

  def send(self):
    payload = self.PARAMS.copy()

    payload.update({
      'phone': self.message.number_list,
      'text': self.message.message
      })

    sms_request = requests.get(self.API_BASE_URL.MESSAGE, params=payload)

    message_id = sms_request.content
    response_code = sms_request.status_code

