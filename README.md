# API Guide
![Deploy](https://github.com/Dieform-Automation/API/workflows/Deploy/badge.svg)


# Live API Link + Swagger UI
https://shielded-lake-43806.herokuapp.com/

## Customer
| Method | Action | Endpoint  | Arguments | Body | Complete |
|---|---|---|---|---|:---:|
|GET | Get all customers | /customer/ | - | - | <ul><li>- [x] </li></ul> |
|GET | Get customer by id |  /customer/id | - | - | <ul><li>- [x] </li></ul>  |
|POST| Add customer | /customer/ | -  | name, point_of_contact, email, street, city, province, country, postal code, phone | <ul><li>- [x] </li></ul>  |
|PUT| Update customer | /customer/id | - | name, point_of_contact, email, street, city, province, country, postal code, phone | <ul><li>- [x] </li></ul>  |

## Part
| Method | Action | Endpoint  | Arguments | Body | Complete |
|---|---|---|---|---|:---:|
|GET | Get all parts | /part/ | - | - | <ul><li>- [x] </li></ul> |
|GET | Get part by id |  /part/id | - | - | <ul><li>- [x] </li></ul>  |
|GET | Get all parts by customer_id |  /part? | customer_id | - | <ul><li>- [x] </li></ul>  |
|POST| Add part | /part/ | - | number, name, purchase_order_id, customer_id | <ul><li>- [x] </li></ul>  |
|PUT| Update part | /part/id | - | name | <ul><li>- [x] </li></ul>  |

## Purchase Order
| Method | Action | Endpoint  | Arguments | Body | Complete |
|---|---|---|---|---|:---:|
|GET | Get all purchase orders and associated parts | /purchase_order/ | - | - | <ul><li>- [x] </li></ul> |
|GET | Get purchase order by id |  /purchase_order/id | - | - | <ul><li>- [x] </li></ul>  |
|GET | Get all orders by customer_id |  /purchase_order? | customer_id | - | <ul><li>- [x] </li></ul>  |
|POST| Add order | /purchase_order/ | - | customer_id, number | <ul><li>- [x] </li></ul>  |

## Receiving Order
| Method | Action | Endpoint  | Arguments | Body | Complete |
|---|---|---|---|---|:---:|
|GET | Get all receiving orders | /receiving_order/ | - | - | <ul><li>- [x] </li></ul> |
|GET | Get receiving order by id |  /receiving_order/id | - | - | <ul><li>- [x] </li></ul>  |
|GET | Get all receiving orders by customer_id |  /receiving_order? | customer_id | - | <ul><li>- [x] </li></ul>  |
|POST| Add receiving order | /receiving_order/ | - | customer_id, customer_packing_slip, date* [format: "month/day/year hour:minute:second"] | <ul><li>- [x] </li></ul>  |
|PUT| Update receiving order | /receiving_order/id | - | customer_packing_slip | <ul><li>- [x] </li></ul>  |
