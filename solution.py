# Write your code below: 
from contextlib import contextmanager
@contextmanager
def generic(card_type, sender_name, recipient):
  card = open(str(card_type), 'r')
  new_card = open(str(sender_name) + "_generic.txt", 'w')
  try:
    new_card.write("Dear " + str(recipient) + ", \n" + str(card.read()) + "\nSincerely, \n" + str(sender_name))
    yield new_card
  finally:
    card.close()
    new_card.close()
with generic('thankyou_card.txt', 'Mwenda', 'Amanda'):
  print('Card Generated!')
with open('Mwenda_generic.txt', 'r') as final_card:
  print(final_card.read())
class personalized:
  def __init__(self, sender_name, recipient):
    self.sender_name = sender_name
    self.recipient = recipient
    self.new_card = open(str(sender_name) + "_personalized.txt", 'w')
  def __enter__(self):
    self.new_card.write("Dear " + str(self.recipient) + ", \n")
    return self.new_card
  def __exit__(self, exc_type, exc_value, Traceback):
    self.new_card.write("\nSincerely, \n" + str(self.sender_name))
    self.new_card.close()
with personalized('John', 'Michael') as card:
  card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")
with open("John_personalized.txt", 'r') as card1:
  print(card1.read())
with generic('happy_bday.txt', 'Josiah', 'Remy'):
  print('Card Generated!')
with open('Josiah_generic.txt', 'r') as final_card:
  print(final_card.read())
with personalized('Josiah', 'Esther') as card:
  card.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")
with open("Josiah_personalized.txt", 'r') as card1:
  print(card1.read())