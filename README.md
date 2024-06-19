# Restaurant Reservation App

A command-line application for managing restaurant reservations.

## Features
- Create and manage restaurants, tables, reservations, and customers
- Command-line interface for easy interaction
- Database persistence using SQLite and SQLAlchemy

## Installation
1. Clone the repository
2. Install dependencies: `pipenv install`
3. Set up the database: `pipenv run restaurant-reservation create-tables`

## Usage
- Create a new reservation: `pipenv run restaurant-reservation create-reservation`
- List all reservations: `pipenv run restaurant-reservation list-reservations`
- Update a reservation: `pipenv run restaurant-reservation update-reservation`
- Delete a reservation: `pipenv run restaurant-reservation delete-reservation`

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.