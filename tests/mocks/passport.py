"""Mock data for passport"""
import uuid
import datetime

VALID_PASSPORT_DETAILS = {
   "id": str(uuid.uuid4()),
   "userId": 'fdadbc7e-3e94-4834-a91a-341fe63e1166',
   "passportType": 'P',
   "nationality": 'nigerian',
   "passportNumber": 'B098712345',
   "dateOfBirth": '1990-01-9 13:00:00',
   "sex": 'male',
   "dateOfIssue": '2019-02-14 00:00:00',
   "dateOfExpiry": '2023-02-14 00:00:00'
}
