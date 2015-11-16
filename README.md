# API

## /login [POST]

## /logout [POST]

## /offers [GET, POST]
### GET
Returns a list of all offers that are of certain distance from
certain points
### POST
Create a new offer

## /offers/<offer-id> [GET, PUT, DELETE]
### GET
Return <offer-id>'s details
### PUT
Modify <offer-id>'s details
### DELETE
Delete <offer-id>

## /user [POST]
Create new user

## /user/<user-id> [GET, PUT]
### GET
Return <user-id>'s details
### PUT
Modify <user-id>'s details

The endpoints should be prefixed with API version ('/api/v1', or so)
