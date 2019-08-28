"""Mock data for passport"""
import uuid
import datetime

VALID_PASSPORT_DETAILS = {
   "id": str(uuid.uuid4()),
   "userId": 'fdadbc7e-3e94-4834-a91a-341fe63e1166',
   "passportType": 'P',
   "nationality": 'nigerian',
   "passportNumber": 'B098712345',
   "dateOfBirth": '1990-01-9',
   "sex": 'male',
   "dateOfIssue": '2019-02-14',
   "dateOfExpiry": '2023-02-14'
}

VALID_PASSPORT_DATA = {
    "userId": 'fdadbc7e-3e94-4834-a91a-341fe63e1166',
    "passportType": 'P',
    "nationality": 'nigerian',
    "passportNumber": 'B098712345',
    "dateOfBirth": '1990-01-9',
    "sex": 'male',
    "dateOfIssue": '2019-02-14',
    "dateOfExpiry": '2023-02-14'
}

VALID_PASSPORT_DATA_TWO = {
    "userId": 'mmadbc7e-3e94-4834-a91a-341nn63e1166',
    "passportType": 'P',
    "nationality": 'nigerian',
    "passportNumber": 'B098321745',
    "dateOfBirth": '1993-01-9',
    "sex": 'female',
    "dateOfIssue": '2019-02-19',
    "dateOfExpiry": '2023-02-19'
}

INVALID_PASSPORT_DATA_ONE = {
    "userId": 'kmadbc7e-3e94-4834-a91a-341nn00e2266',
    "passportType": 'P',
    "nationality": 'nigerian',
    "passportNumber": 'B098344745',
    "dateOfBirth": '1993-01-9',
    "sex": 'female',
    "dateOfIssue": '2019-02-19',
    "dateOfExpiry": '2019-01-19'
}

INVALID_PASSPORT_DATA_TWO = {
    "userId": 'cccryc7e-3e94-3448-a91a-341nn00e7755',
    "passportType": 'P',
    "nationality": 'nigerian',
    "passportNumber": 'K098388850',
    "dateOfBirth": '2100-01-9',
    "sex": 'male',
    "dateOfIssue": '2019-01-19',
    "dateOfExpiry": '2019-02-19'
}

INVALID_PASSPORT_DATA_THREE = {
    "userId": 'mmadbc7e-3e94-4834-a91a-341nn63e1166',
    "passportType": 'P',
    "nationality": 'nigerian',
    "passportNumber": 'B098321745',
    "dateOfBirth": '1993-01-9',
    "sex": 'female',
    "dateOfIssue": '2019-02-19',
    "dateOfExpiry": '2023-02-19'
}
