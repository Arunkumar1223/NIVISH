x = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'Nivish_staging',
        # # Manikanta Commented port setting for database configuration, to be used only if database is on another instance
        'CLIENT': {
            'host': '3.111.107.34',
            'port': 27017,
            'username': 'devops_admin',
            'password': 'Devops@1234',
            'authsource': 'admin',
        }
    }}

AWS_ACCESS_KEY_ID = 'AKIAVUQMV7NGTJBURAUJ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'vfydevexperiments'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'