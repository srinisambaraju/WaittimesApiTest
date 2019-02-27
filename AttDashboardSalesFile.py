from selenium import webdriver
from datetime import datetime
import zipfile
from os import os, path, remove
import pysftp
from driver_builder import DriverBuilder
from time import sleep


class TestDownload:
    def test_download(self):

        driver_builder = DriverBuilder()

        download_path = path.dirname(path.realpath(__file__))

        expected_download = path.join(download_path, "5MB.zip")

        # clean downloaded file
        try:
            remove(expected_download)
        except OSError:
            pass

        assert (not path.isfile(expected_download))

        driver = driver_builder.get_driver(download_path, headless=True)

        driver.get("https://www.thinkbroadband.com/download")

        clone_box = driver.find_element_by_xpath('//*[@id="main-col"]/div/div/div[8]/p[1]/a/img')
        clone_box.click()

        self.wait_until_file_exists(expected_download, 30)
        driver.close()

        assert (path.isfile(expected_download))

        print("done")

    def wait_until_file_exists(self, actual_file, wait_time_in_seconds=5):
        waits = 0
        while not path.isfile(actual_file) and waits < wait_time_in_seconds:
            print("sleeping...." + str(waits))
            sleep(.5)  # make sure file completes downloading
            waits += .5


def sftp_upload(edi_file):
    host = "s-8cfcba85595d4d749.server.transfer.us-east-1.amazonaws.com"
    user_name = "springdealerworkspaceuser"
    private_key = "add the private key here"
    try:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        # Define the actual SFTP connection
        with pysftp.Connection(host=host, port=22, username=user_name,
                               private_key="dHJhbnNmZXIta2V5", cnopts=cnopts) as sftp:
            with sftp.cd("/to some directory/directory"):
                sftp.put("tmp/{}".format(edi_file))
                # once the upload is done return a success message
                # at this point return or send an email to stake holders that the file is uploaded to SFTP
                return 'ATT Dashboard Metrics file {} has been uploaded successfully'.format(edi_file)
    except(IOError, OSError):
        return 'Att Dashboard Metrics file {} failed to upload'.format(edi_file)


pathtodownloaddirectory = "C:\Downloads\AttDashboard"
prefs = {"download.default_directory": pathtodownloaddirectory}

# "browser.set_download_behavior":
#         {"behavior": "allow", "downloadPath": path_to_download_directory}}
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)
# options.add_argument("headless")
# options.add_argument("window-size=1200x600")

driver = webdriver.Chrome(chrome_options=options)

# This is set to 50 seconds to implicitly wait before going in to find the element you are looking for, because
# sometimes the page load takes time and setting it a number like this will make it wait till the element is visible
# and can be extracted
driver.implicitly_wait(50)

driver.get("https://www.e-access.att.com/dws/dwsPortal/listReport.do")
# Need to add this UserName and password in a configuration file in secure way
userid_elem = driver.find_element_by_xpath('//*[@id="lrrFormId"]/table[3]/tbody/tr[2]/td/table/tbody/tr[3]/td/'
                                           'table/tbody/tr[1]/td/input')
userid_elem.send_keys("XD17669126")

password_elem = driver.find_element_by_xpath('//*[@id="lrrFormId"]/table[3]/tbody/tr[2]/td/table/tbody/tr[3]/td/table/'
                                             'tbody/tr[3]/td/input')
password_elem.send_keys("NewPasswordRequirement")

# This is the Login button click
driver.find_element_by_xpath('//*[@id="lrrFormId"]/table[3]/tbody/tr[2]/td/table/tbody/tr[3]/td/table/'
                             'tbody/tr[5]/td/input').click()

# After logging in there is another "OK" button that needs to be clicked to confirm that its the USer who you are
# supposed to be
driver.find_element_by_xpath('//*[@id="srv_successok"]/input').click()

# In this report there is another acknowledge button which needs to be checked
acknowledge_elem = driver.find_element_by_xpath(
    '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td/input').click()
# After the acknowledge is checked you need to click the login button to get to the page you are looking for.
login_elem = driver.find_element_by_xpath(
    '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/form/table[2]/tbody/tr[2]/td/input[1]').click()
# The actual page where the report shows up takes little while and this is where implicitly_wait comes in handy

# This below element is where you are clicking on "Reports" tab
reports_elem = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[5]/td[2]/a[2]').click()

# AFter the reports tab clicked you are clicking on the selection box where different types of reports available and
# we need "Sales report"
report_type_sales_selection = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/table/'
                                                           'tbody/tr[1]/td/form/table[2]/tbody/tr[2]/td[2]/'
                                                           'select/option[5]').click()

# The below is to extract the text from the Report date column to ensure that we are downloading the latest report
currentmonth_elem = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/'
                                                 'tr[4]/td[7]')
actual_month = datetime.now().strftime('%B') + ' ' + datetime.now().strftime('%Y')
if actual_month == currentmonth_elem.text:
    print(currentmonth_elem.text)
    current_month_input_checkbox = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr/td/'
                                                                'table/tbody/tr[4]/td[1]/input').click()
    currentelemdownload = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/div/table/tbody/tr/td[1]/'
                                                       'table/tbody/tr/td/input').click()
    fileExists = False
    my_path = 'C:/Downloads/AttDashboard/'
    # want to check if the fileexists in the directory and then gracefully come out of the whole automation
    # There might be a better way to do this, but for now this Works Amazing!
    done = False
    file_path = ''
    file_extracted = False
    while not fileExists:
        for root, dirs, files in os.walk(my_path):
            print(root, dirs, files)
            print('Inside')
            for file in files:
                if file.endswith('.zip'):
                    print(os.path.join(root, file))
                    file_path = os.path.join(root, file)
                    done = True
                    fileExists = True
                    break
            if done:
                break

        if fileExists:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(my_path)
                file_extracted = True
            break
# You can close the browser now, no need to keep that open. The better way to do it is by Logging off.
driver.close()
if file_extracted:
    done = False
    os.remove(file_path)
    for root, dirs, files in os.walk(my_path):
        for file in files:
            print("file name is " + file)
            if file.endswith('.zip'):
                file_path = os.path.join(root, file)
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(my_path)
                    done = True
                break
        if done:
            break
    os.remove(file_path)
    # We need to upload the file to SFTP here, but before that we need to get the name of the file from the folder that
    # needs to be uploaded
    # HAVEN'T TESTED THE BELOW CODE BUT SOMETHING ALONG THOSE LINES - THIS IS DONE, PROJECT IS DONE
#    for item in os.listdir(my_path):  # loop through items in dir
#        if item.endswith('.dat'):
#            file_path = os.path.join(my_path, item)
#            sftp_upload(file_path)
#        break
