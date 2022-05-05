from msvcrt import kbhit
from kq_login import login 
from kq_mail import mail
from kq_board import board
from kq_task import task
from kq_whisper import whisper
from kq_approval  import approval
from kq_contact import contact
from kq_project import project
from kq_archive import archive

if login() == True :
    mail()
    board()
    task()
    whisper()
    approval()
    contact()
    project()
    archive()
