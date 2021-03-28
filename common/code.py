from enum import Enum


class Code(Enum):

    OK = '0'
    USERNAME_PASSWORD_MISMATCH = '10001'
    SMS_CODE_MISMATCH = '10002'

    TENANT_NO_ACCESS = '10003'

    SMS_PROVIDER_IS_MISSING = '11001'