
def assume_role:
    sts = boto3.client('sts')

    assumed_role_arn = os.getenv('ASSUMED_ROLE')

    #sts provides temporary credentials for accessing AWS resources across accounts. 
    assumed_role_object=self.sts.assume_role(
                RoleArn=assumed_role_arn,
                RoleSessionName="AssumeRoleSession1")

    creds=self.assumed_role_object.get('Credentials')

    #invoke lambda in seperate account 
    self._client_la=boto3.client(
                    'lambda',
                    aws_access_key_id=self.credentials.get('AccessKeyId'),
                    aws_secret_access_key=self.credentials.get('SecretAccessKey'),
                    aws_session_token=self.credentials.get('SessionToken'),
                )

        