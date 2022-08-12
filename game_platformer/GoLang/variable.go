package main

import (
	"fmt"
	"strings"
)

func main() {
	conferenceName := "Go Conference" // another way to initialize a variable without datatype
	const conferenceTickets = 50      //a constance variable cannot change
	var remainingTickets = 50
	fmt.Printf("conferenceName is %T , conferenceTickets is %T , reaminingTickets is %T\n", conferenceName, conferenceTickets, remainingTickets)
	fmt.Printf("Welcome to %v Booking appllication.", conferenceName)
	// %v only have in Printf not have in Println
	fmt.Println("We have total ", conferenceTickets, "tikets and ", remainingTickets, "are still available")
	fmt.Println("Get your tickets here to attend this conference")

	var FirstName string
	var LastName, email string
	var userTickets int
	//Ask user for their name
	fmt.Printf("Enter your First Name :")
	fmt.Scan(&FirstName) // this is the poiter and & is memory adress of userName
	fmt.Printf("Enter your Last Name :")
	fmt.Scan(&LastName)
	fmt.Printf("Enter your Email :")
	fmt.Scan(&email)
	fmt.Printf("Enter the number tickets you want :")
	fmt.Scan(&userTickets)

	remainingTickets = remainingTickets - userTickets

	fmt.Printf("Username : %v \n", FirstName+" "+LastName)
	fmt.Printf("Email : %v \n", email)
	fmt.Printf("Tikets : %v \n", userTickets)

	fmt.Printf("The remaining Tickets is : %v \n", remainingTickets)

	//Array
	bookings := []string{"Hello"}
	//bookings[0] = FirstName + " " + LastName
	Name := []string{"World"}
	//Name[0] = LastName + " " + FirstName
	// bookings[1] = "Akimichi"
	bookings = append(bookings, Name...)

	fmt.Println("The whole array : ", bookings)

	for index, booking := range bookings {

		var names = strings.Fields(booking)
		var FirstName = Name[0]
		//fmt.Printf("%v \t %v \n", index, booking)

	}

}
