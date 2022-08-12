package main

import "fmt"

func main() {
	var FirstName string
	var LastName string
	//Ask user for their name
	fmt.Printf("Enter your First Name :")
	fmt.Scan(&FirstName) // this is the poiter and & is memory adress of userName
	fmt.Printf("Enter your Last Name :")
	fmt.Scan(&LastName)
	//Array
	bookings := []string{FirstName + " " + LastName}
	//bookings[0] = FirstName + " " + LastName
	Names := []string{"Alimohamed", "Goodjob"}
	Names[0] = LastName
	// bookings[1] = "Akimichi"
	bookings = append(bookings, Names[0])
	fmt.Println("The whole array : ", bookings)

	// for index, booking := range bookings {

	// 	fmt.Printf("%v \t %v \n", index, booking)

	// }

}
