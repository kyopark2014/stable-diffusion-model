# Cloud9 설치

## EC2 생성 

[EC2 console](https://ap-northeast-2.console.aws.amazon.com/ec2/home?region=ap-northeast-2#LaunchInstances:)에 접속하여 [Name]을 입력하고, OS로 "Ubuntu"를 선택합니다. 여기서는 [Name]으로 "cloud9-gpu"라고 입력하였습니다. 

![noname](https://user-images.githubusercontent.com/52392004/216653942-3f7ce41e-931d-4a60-8672-33e723b30a8f.png)

적절한 Instance Type을 선정합니다. 여기서는 p3.2xlarge를 선택하였습니다. 이후 key pair를 설정하고, 아래처럼 Strage 크기도 조정하고 [Launch Instance]를 선택하여 EC2를 생성합니다. 

![noname](https://user-images.githubusercontent.com/52392004/216655203-0ead79d8-0c6d-422c-ae10-a952f3efc420.png)

## Cloud9 생성

[Cloud9 Console](https://ap-northeast-2.console.aws.amazon.com/cloud9control/home?region=ap-northeast-2#/create)에서 아래와 같이 [Name]을 입력하고, [Existing compute]를 선택한 후에 [Copy key to clipboard]를 선택하여 ssh key를 복사합니다. 여기서는 Name으로 "cloud9-gpu"라고 입력하였습니다. 

![noname](https://user-images.githubusercontent.com/52392004/216656333-24d9347a-8564-4018-93ec-0e38a0e7ade2.png)

[EC2 Console](https://ap-northeast-2.console.aws.amazon.com/ec2/home?region=ap-northeast-2#Instances:)로 이동하여, 생성한 EC2를 선택하고 [Connect]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/216657296-77e8b81a-d287-4a50-ae17-8137c845bdbe.png)

아래와 같이 [Connect to instances]에서 [Connect]를 선택합니다. 

![noname](https://user-images.githubusercontent.com/52392004/216657819-4fd9629b-a000-4d1b-a602-ef6971a698ed.png)

이제 authorized_keys에 Cloud9에서 복사한 ssh key를 입력합니다. 

```java
echo <Paste the Copied Key> >> ~/.ssh/authorized_keys
```

아래와 같이 입력됩니다. 

![noname](https://user-images.githubusercontent.com/52392004/216660260-e01667b7-1c5c-41db-8539-ff5b9ac8d6ea.png)


필요한 패키지를 설치하기위해 먼저 Update를 수행합니다. 

```java
sudo apt-get update
```

아래와 같이 pip python2.7과 node.js를 설치합니다.

```java
sudo apt-get install -y pip python2 nodejs
```

다시 Cloud9으로 와서 [User]에 "ubuntu"라고 입력하고, 생성한 EC2의 Public IP를 아래처럼 입력합니다. 이후 하단의 [Create]를 선택하여 Cloud9을 선택합니다. 


![noname](https://user-images.githubusercontent.com/52392004/216661248-2fb846d2-4e07-435d-8b79-d4f8d037c206.png)


아래와 같이 [Environment]에서 생성한 "cloud9-gpu"에서 [Open]을 선택하여 cloud9으로 진입합니다. 이대 아래와 같은 화면이 나오면 [Next]를 선택합니다.

![image](https://user-images.githubusercontent.com/52392004/216662019-28f065d7-88a5-4ad5-8182-9362751a63d9.png)

아래와 같이 Installer에서도 [Next]를 선택하여 필요한 패키지를 설치합니다. 수분정도 소요됩니다. 

![image](https://user-images.githubusercontent.com/52392004/216662159-5ff76f78-7beb-4365-871e-dbbd4d23e912.png)

설치가 완료되면 아래와 같이 터미널로 접속합니다. 

![noname](https://user-images.githubusercontent.com/52392004/216664493-8fa9c618-8ab1-4ea1-8563-74a94ee27aef.png)
