import boto3


#Nik
clientId   = ""
userPoolId = ""

username = "user1"
new_password = ""
first_password = ""

auth = {
    "USERNAME": username,
    "PASSWORD": new_password,
}

auth_first = {
    "USERNAME": username,
    "PASSWORD": first_password,
}

auth_reset_password = {
    "USERNAME": username,
    "NEW_PASSWORD": new_password,
}

session = boto3.Session(profile_name="default")
client  = session.client("cognito-idp", "us-east-1")

def change_password():
    response = client.admin_initiate_auth(
        UserPoolId=userPoolId,
        ClientId=clientId,
        AuthFlow="ADMIN_NO_SRP_AUTH",
        AuthParameters=auth_first
    )

    print(response)

    response = client.respond_to_auth_challenge(
        ClientId=clientId,
        ChallengeName="NEW_PASSWORD_REQUIRED",
        Session=response["Session"],
        ChallengeResponses=auth_reset_password
    )
    
    print(response)

def get_token():
    response = client.admin_initiate_auth(
        UserPoolId=userPoolId,
        ClientId=clientId,
        AuthFlow="ADMIN_NO_SRP_AUTH",
        AuthParameters=auth
    )
    return response["AuthenticationResult"]["IdToken"]

def main():
    try:
        change_password()
    except:
        pass
    token = get_token()
    print(f"ID token: {token}")

if __name__ == "__main__":
    main()
