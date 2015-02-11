import requests

class BhashSMSIntegration():
  USERNAME = 'imgiitr'
  PASS = 'imgiitrsms'
  SENDER_ID = 'IMGSRE'

  PARAMS = {
    'user': USERNAME,
    'pass': PASS,
    'sender': SENDER_ID,
    'priority': 'ndnd',
    'smstype': 'normal'
  }

  REPORT_PARAMS = {
    'user': USERNAME,
    'msgtype': 'ndnd'
  }

  API_BASE_URL = {
    'MESSAGE': 'http://bhashsms.com/api/sendmsg.php',
    'DELIVERY_REPORT': 'http://bhashsms.com/api/recdlr.php'
  }

  class Meta:
    abstract = True

  def __init__(self, message):
    self.message = message

  def send(self):
    payload = self.PARAMS.copy()

    payload.update({
      'phone': self.message.get('number_list'),
      'text': self.message.get('message')
      })

    sms_request = requests.get(self.API_BASE_URL.get('MESSAGE'), params=payload)

    response_content = sms_request.content
    response_code = sms_request.status_code

    number_list = self.message.get('number_list').split(',')
    message_ids = response_content.split()
    status_list = []

    for i in range(0,len(number_list)):
      status = self.delivery_status(number_list[i], message_ids[i])
      status_list.append(status)

    self.message.update({
      'message_ids': ','.join(message_ids),
      'status_list': ','.join(status_list),
      'response_code': response_code
      })

    return self.message

  def delivery_status(self, number, message_id):
    payload = self.REPORT_PARAMS.copy()

    payload.update({
        'phone': number,
        'msgid': message_id
      })

    delivery_report = requests.get(self.API_BASE_URL.get('DELIVERY_REPORT'), params=payload)

    return delivery_report.content
