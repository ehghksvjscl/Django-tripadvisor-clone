DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "tripadvisor",
        "USER": "root",
        "PASSWORD": "rktn4156",
        "HOST": "drmozart.cl2mk0mgzle0.us-east-2.rds.amazonaws.com",
        "PORT": "3306",
        "TEST": {"CHARSET": "utf8", "COLLATION": "utf8_general_ci",},
        "OPTIONS": {"init_command": 'SET sql_mode="STRICT_TRANS_TABLES"'},
    }
}

SECRET_KEY = "tripadvisor"

ALGORITHM = 'HS256'

AWS_ACCESS_KEY_ID = 'AKIAXP4NZNEW3KPJECJP'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'wecode-tripadviser'
S3URL = 'https://wecode-tripadviser.s3.ap-northeast-2.amazonaws.com/'
