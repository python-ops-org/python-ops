



Phase-01

API traffic → API Gateway → Go Backend
Video traffic → Nginx docker on EC2 → MediaMTX



Video Traffic

Internet
   │
stream.retinahalo.com
   │
Nginx (Docker) - EC2 t4g.small
   │
MediaMTX (Docker) - EC2 t4g.small
   │
IP Cameras / DVRs / NVRs
   │
WebRTC / HLS / RTSP Viewers

────────────────────────────────────

AI Analytics

Frigate - EC2 t4g.medium
   │
Object Detection
Motion Detection
Face Recognition (Future)
Vehicle Detection (Future)
   │
S3
   ├── Clips
   ├── Snapshots
   └── Backups


Cognito for authentication and session management
API Gateway + Lambda for login, OTP, payments, notifications
Go API for business logic
PostgreSQL for metadata
MediaMTX + Nginx for video streaming
Frigate + S3 for AI analytics and storage



Cognito
├── Full_Name
├── Email
├── Phone_Number
├── Email_Verification
├── OTP_Authentication
├── User_Groups
└── JWT_Tokens / Sessions

PostgreSQL
├── Customers
├── Sites
├── Cameras
├── Recordings
├── AI_Events

├── Subscriptions
├── Storage_Plans
├── Audit_Logs
├── Storage_Usage
├── Device_Inventory
├── Camera_Health
├── Payment_Transactions
└── Notifications

Customers
├── id
├── cognito_user_id
├── email
├── company_name
├── plan
├── status
├── created_at
└── updated_at


Sites
├── id
├── customer_id
├── site_name
├── address
├── timezone
├── created_at
└── updated_at


Cameras
├── id
├── site_id
├── camera_name
├── camera_type
├── rtsp_url
├── status
├── created_at
└── updated_at


Storage_Plans
├── id
├── plan_name
├── storage_limit_gb
├── retention_days
├── max_cameras
├── ai_enabled
├── monthly_price
├── active
├── created_at
└── updated_at


customer.go
   │   ├── Customer Management
   │   └── User Profile APIs
   │
   ├── site.go
   │   ├── Site Management
   │   └── Location Management
   │
   ├── camera.go
   │   ├── Camera Onboarding
   │   ├── Camera Configuration
   │   ├── Camera Health
   │   └── Multi-View Management
   │
   ├── recording.go
   │   ├── Recording Search
   │   ├── Recording Metadata
   │   └── Clip Management
   │
   ├── storage.go
   │   ├── Storage Manager
   │   ├── S3 Operations
   │   └── Retention Policies
   │
   ├── event.go
   │   ├── AI Events
   │   ├── Motion Events
   │   └── Alert APIs
   │
   ├── billing.go
   │   ├── Billing APIs
   │   ├── Subscription APIs
   │   └── Plan Management
   │
   └── health.go
       ├── Health Checks
       ├── Metrics
       └── Readiness Probes



R__seed_storage_plans.sql
V1__core_schema.sql
V2__recordings_ai.sql
V3__subscriptions_storage.sql
V4__device_monitoring.sql
V5__notifications_payments_audit.sql



 
Cognito:
User authentication, authorization, OTP verification, user profiles, groups, and JWT management.

PostgreSQL:
Primary database for all RetinaHalo application, CCTV, customer, billing, storage, and AI event data.

Redis:
Future caching layer for sessions, rate limiting, dashboard performance, and metadata caching.




Phase 2
---------
camera.go

Phase 3
---------
recording.go

Phase 4
---------
storage.go

Phase 5
---------
event.go

Phase 6
---------
billing.go

Phase 7
---------
health.go


Frontend (Next.js)
      |
AWS Amplify Hosting
      |
Cloudflare
      |
Public ALB
      |
ECS EC2 ARM Cluster
------------------------------------------------
| Go API Service                               |
| MediaMTX Service                             |
| Frigate Service                              |
------------------------------------------------
      |
Motion / Object Detection
      |
Event Clip & Snapshot Generation
      |
Upload Event Clips to S3
      |
S3 Lifecycle Policies
      |
Glacier / Deep Archive













                   ┌──────── Live Streaming ────────┐
                   │                                ↓
IP Camera → Edge → Kinesis → WebRTC/HLS → CloudFront → App
                   │
                   ├──── Cloud Analytics ───────────┐
                   │                                ↓
                   │          Rekognition / SageMaker
                   │                                ↓
                   │             Events & Alerts (SNS)
                   │
                   └──── Surveillance Storage ──────┐
                                                    ↓
                                            Amazon S3 → Glacier



OTP-based authentication (passwordless)

✅ JWT tokens from Cognito

✅ API Gateway JWT authorizer

✅ No credential storage in your code

✅ IAM isolation between services

✅ No direct DB exposure to frontend

✅ CAPTCHA on auth page

✅ Idle time session expiration




retina-auth/
├── cmd/
│   ├── send-otp/
│   │   └── main.go     -> Lambda #1
│   └── verify-otp/
│       └── main.go     -> Lambda #2
├── internal/
│   ├── cognito/
│   │   └── client.go
│   └── utils/
│       └── response.go
├── go.mod



User Enters Email
        │
        ▼
API Gateway
        │
        ▼
Lambda (login.py)
        │
        ▼
Cognito Lookup
        │
   User Exists?
        │
        ▼
Generate OTP
        │
        ▼
SES Email
        │
        ▼
User Enters OTP
        │
        ▼
Cognito Verification
        │
        ▼
JWT Token
        │
        ▼
Frontend Stores Token
        │
        ▼
API Gateway
        │
        ▼
Go Backend APIs







Amplify (Next.js)
   │
Cognito
   ├── Full_Name
   ├── Email
   ├── Phone_Number
   ├── Email_Verification
   ├── OTP_Authentication
   ├── User_Groups
   └── JWT_Tokens / Sessions
   │
API Gateway (api.retinahalo.com)
   │
Lambda
   ├── login.py
   │   ├── Cognito User Lookup
   │   ├── OTP Generation
   │   ├── OTP Verification
   │   └── JWT Token Issuance
   │
   ├── payment.py
   │   ├── Razorpay Order Creation
   │   ├── Payment Verification
   │   ├── Subscription Activation
   │   └── Payment Webhooks
   │
   └── notification.py
       ├── SES Email Notifications
       ├── Welcome Emails
       ├── Billing Alerts
       ├── Storage Alerts
       └── System Notifications

   │
Docker Go Backend (stream.retinahalo.com) on EC2 t4g.small (Ready for Future Horizontal Scaling)

   ├── customer.go
   │   ├── Customer Management
   │   └── User Profile APIs
   │
   ├── site.go
   │   ├── Site Management
   │   └── Location Management
   │
   ├── camera.go
   │   ├── Camera Onboarding
   │   ├── Camera Configuration
   │   ├── Camera Health
   │   └── Multi-View Management
   │
   ├── recording.go
   │   ├── Recording Search
   │   ├── Recording Metadata
   │   └── Clip Management
   │
   ├── storage.go
   │   ├── Storage Manager
   │   ├── S3 Operations
   │   └── Retention Policies
   │
   ├── event.go
   │   ├── AI Events
   │   ├── Motion Events
   │   └── Alert APIs
   │
   ├── billing.go
   │   ├── Billing APIs
   │   ├── Subscription APIs
   │   └── Plan Management
   │
   └── health.go
       ├── Health Checks
       ├── Metrics
       └── Readiness Probes

   │
PostgreSQL
(Private EC2 t4g.small)
(Vertical Scaling)

   ├── Customers
   ├── Sites
   ├── Cameras
   ├── Recordings
   ├── AI_Events
   ├── Billing
   ├── Subscriptions
   ├── Storage_Plans
   ├── Audit_Logs
   ├── Storage_Usage
   ├── Device_Inventory
   ├── Camera_Health
   ├── Payment_Transactions
   └── Notifications

Backup Strategy
   ├── Daily PostgreSQL Snapshots
   ├── WAL Backups
   └── EBS Snapshots








https://egng1et5i1.execute-api.ap-south-1.amazonaws.com/email-booking

{
  "service": "CCTV Installation",
  "property": "Apartment / Flat",
  "cameras": "1 - 4",
  "name": "Sudipta Chakraborty",
  "phone": "9766451481",
  "date": "2026-06-17",
  "email": "sudipta78645@gmail.com"
}



curl -X POST \
https://egng1et5i1.execute-api.ap-south-1.amazonaws.com/email-booking \
-H "Content-Type: application/json" \
-d '{
  "service":"CCTV Installation",
  "property":"Apartment / Flat",
  "cameras":"1 - 4",
  "name":"Sudipta Chakraborty",
  "phone":"9766451481",
  "date":"2026-06-17",
  "email":"sudipta78645@gmail.com"
}'
