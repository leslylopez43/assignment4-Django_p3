## Tenant Table

| Field            | Description            |
|------------------|------------------------|
| Tenant ID        | Unique identifier for the tenant      |
| Name             | Tenant's first name     |
| Last Name        | Tenant's last name      |
| DOB              | Tenant's date of birth  |
| Plus 18's        | Number of tenants aged 18 and above   |
| Under 18's       | Number of tenants below 18 years old  |
| Email Address    | Tenant's email address  |
| Mobile Phone     | Tenant's mobile phone number |
| Address          | Tenant's address        |
| Post Code        | Tenant's postal code    |
| Country          | Tenant's country        |
| Billing Address  | Tenant's billing address |
| Billing Post Code| Tenant's billing postal code |
| Billing Country  | Tenant's billing country |

## Tenancy Table

| Field            | Description            |
|------------------|------------------------|
| Accommodation ID | Unique identifier for the accommodation  |
| Tenant ID        | Unique identifier for the tenant  |
| Check-in         | Date and time of check-in  |
| Check-out        | Date and time of check-out |
| Sleeps           | Number of people accommodated |
| Venue Type       | Type of venue (e.g., hall, apartment) |

## Accommodation Table

| Field            | Description            |
|------------------|------------------------|
| Tenant ID        | Unique identifier for the tenant  |
| Accommodation ID | Unique identifier for the accommodation  |

###### Hall Table

| Field            | Description            |
|------------------|------------------------|
| Accommodation ID | Unique identifier for the hall  |
| Weddings         | Availability for weddings |
| Birthdays        | Availability for birthdays |
| Parties          | Availability for parties   |
| Baby Shower      | Availability for baby showers |
| Corporate Events | Availability for corporate events |
| Christmas        | Availability for Christmas events |
| Lilmedshoot & Photoshoot | Availability for lifestyle and photoshoots |

##### Apartments Table

| Field            | Description            |
|------------------|------------------------|
| Accommodation ID | Unique identifier for the apartment  |
| Check-in         | Date and time of check-in  |
| Check-out        | Date and time of check-out |
| Guest            | Number of guests          |
| Rooms            | Number of rooms           |
| Check Availability | Availability of the apartment |

## Payments

| Field              | Description            |
|--------------------|------------------------|
| Tenant ID          | Unique identifier for the tenant  |
| Full Name          | Full name of the tenant  |
| Post Code          | Tenant's postal code    |
| Email Address      | Tenant's email address  |
| Contact Details    | Tenant's contact details  |
| Billing Address    | Tenant's billing address |
| Pay with           | Payment method (e.g., credit card, PayPal) |
| Add new card       | Option to add a new payment card |
| Donate to Charity  | Option to donate to charity |
| Subtotal           | Subtotal amount for the payment |
| Order Total        | Total amount to be paid |

## Business or Owner Name

| Field              | Description            |
|--------------------|------------------------|
| Accommodation ID   | Unique identifier for the accommodation  |
| Name               | Name of the business or owner  |
| Business Name      | Name of the business  |
| Address            | Business or owner's address |
| Email Address      | Business or owner's email address |
| VAT                | VAT (Value Added Tax) information |
