/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.hdsb.gwss.sripada_sam.ics3u.u3;

import java.util.Scanner;



/**
 *
 * @author 1sripadasam
 */
public class Y2KProblemDetector {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here

        // Constants
        
        Scanner input = new Scanner(System.in);

        // Variables
        
        int birthYear, currentYear;
        int age = 0;
        
        String strAge = "";

        // Input
        
        System.out.println("Year of Birth: ");
        birthYear = input.nextInt();
        
        System.out.println("Current Year: ");
        currentYear = input.nextInt();
        
        // Processing
        
        if (currentYear > birthYear) {
            
            age = currentYear - birthYear;
            
        } else if (currentYear < birthYear) {
            
            currentYear += 100;
            age = currentYear - birthYear;
            currentYear -= 100;
        } else {
            
            age = 0;
            
        } if (age != 0) {
            
            strAge = Integer.toString(age);
            
        } else {
            
            strAge = "0 or 100";
            
        }
        
        // Output
        
        System.out.println("Year of Birth: " + birthYear + "\nCurrent Year: " + currentYear + "\nYour Age: " + strAge);
        
    }

    private static int String(int i) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

}
