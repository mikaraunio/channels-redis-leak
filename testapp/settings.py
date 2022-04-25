SECRET_KEY = 'xxxxxxxxxxxxxxxxxx'
DEBUG = False
ALLOWED_HOSTS = ['*']

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        # 'BACKEND': 'channels_redis.pubsub.RedisPubSubChannelLayer',
        'CONFIG': {
            'hosts': ['redis://127.0.0.1:6379/0'],
        },
    },
}
