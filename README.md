# API Guide
![Push Container to Heroku](https://github.com/Dieform-Automation/API/workflows/Push%20Container%20to%20Heroku/badge.svg)

# Live API Link + Swagger UI
https://shielded-lake-43806.herokuapp.com/

## Customer
| Method | Action | Endpoint  | Arguments | Body | Complete |
|---|---|---|---|---|:---:|
|GET | Get all customers | /customer/ | - | - | <ul><li>- [x] </li></ul> |
|GET | Get customer by id |  /customer/id | - | - | <ul><li>- [x] </li></ul>  |
|POST| Add customer | /customer/ | -  | name, point_of_contact, email, street, city, province, country, postal code, phone | <ul><li>- [x] </li></ul>  |
|PUT| Update customer | /customer/id | - | name, point_of_contact, email, street, city, province, country, postal code, phone | <ul><li>- [ ] </li></ul>  |

## Part
| Method | Action | Endpoint  | Arguments | Body | Complete |
|---|---|---|---|---|:---:|
|GET | Get all parts | /part/ | - | - | <ul><li>- [x] </li></ul> |
|GET | Get part by id |  /part/id | - | - | <ul><li>- [x] </li></ul>  |
|GET | Get all parts by customer_id |  /part? | customer_id | - | <ul><li>- [x] </li></ul>  |
|POST| Add part | /part/ | - | number, name, customer_id | <ul><li>- [x] </li></ul>  |
|PUT| Update part | /part/id | - | name | <ul><li>- [x] </li></ul>  |

## Order
| Method | Action | Endpoint  | Arguments | Body | Complete |
|---|---|---|---|---|:---:|
|GET | Get all order | /order/ | - | - | <ul><li>- [ ] </li></ul> |
|GET | Get order by id |  /order/id | - | - | <ul><li>- [ ] </li></ul>  |
|GET | Get all orders by customer_id |  /order? | customer_id | - | <ul><li>- [x] </li></ul>  |
|POST| Add order | /order/ | - | customer_id, order_number, list of part_ids (mapped to quantity) | <ul><li>- [x] </li></ul>  |
|PUT| Update order | /order/id | - | list of part_ids (mapped to quantity) | <ul><li>- [ ] </li></ul>  |
