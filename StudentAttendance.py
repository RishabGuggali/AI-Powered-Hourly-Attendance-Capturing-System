import boto3
import requests
import datetime
import time
import cv2

#Credentials----------------------------------------------------------------------------------
client = boto3.client('rekognition',
                      aws_access_key_id="Add your secret key",
                      aws_secret_access_key="o6sInGT3iWaAztZj3kzm/gcUMbp4CnI54kJQT04i",
                      aws_session_token="FwoGZXIvYXdzECEaDIYUDFobtJnX2oDJVCLBAYop3p7T11dVZL/rjE4nmQQNBQEgYMSXua9XMWaiSGT1v1Giv0j4Txt0883Mrmz4zAlN2RAfXPk4QK6MxHEuEamQ3U4AgrZ4qA4AVv+uvMuGLWmVPwqUk/uK61R/kE3cNN5Bs3qzWYOzZ22z1RB8IT8YDxS81Wz5tZT/rRBXEGODdV6oIR8LIYixYoyBfl3hPWxTpqS/IrOzTcFnFbuoLYZQvLH2IGzf087tsV2bL56CoX62V9eAbv8VORF1RlGowgIouvqB/AUyLXdmJoVk+HOLePDbLDlYvDU3e7po7lEVq9DW+Aa3vDoqnjqqCEy3WjQtPj8N5Q==",
                      region_name='us-east-1')

#Capture images for every 1 hour and store the image with current date and time -----------------------------------------------------------------------------------
for j in range(0, 6):
    current_time = datetime.datetime.now().strftime("%d-%m-%y  %H-%M-%S ")
    print(current_time)
    camera = cv2.VideoCapture(0)
    for i in range(20):
        return_value, image = camera.read()
        if (i == 19):
            cv2.imwrite('Hourly Class Images/' + current_time + '.jpg', image)
    del (camera)

#Send the captured image to AWS S3 Bucket--------------------------------------------------------------------------------------
    clients3 = boto3.client('s3', region_name='us-east-1')
    clients3.upload_file("Hourly Class Images/"+current_time+'.jpg', 'add your S3 bucket name', current_time+'.jpg')

    #Recoginze students in captured image ---------------------------------------------------------------------------------------
    with open(r'Hourly Class Images/DonaldTrump.jpg','rb') as source_image:
        source_bytes = source_image.read()
    print(type(source_bytes))

    print("Recognition Service")
    response = client.detect_custom_labels(
        ProjectVersionArn='arn:aws:rekognition:us-east-1:883855801474:project/students/version/students.2020-10-04T13.19.14/1601797754342',

        Image={
            'Bytes': source_bytes
        },

    )

    print(response)
    if not len(response['CustomLabels']):
         print('Not identified')

    else:
        str = response['CustomLabels'][0]['Name']
        print(str)
        # Update the attendance of recognized student in DynamoDB by calling the API
        url = "https://a28j2ku5qb.execute-api.us-east-1.amazonaws.com/test?Rollno=" + str
        resp = requests.get(url)
        print(resp)
        if resp.status_code==200:
            print("Success")

    time.sleep(3600)
