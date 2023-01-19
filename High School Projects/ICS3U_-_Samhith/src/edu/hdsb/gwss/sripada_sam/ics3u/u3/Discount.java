/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.hdsb.gwss.sripada_sam.ics3u.u3;

import java.text.NumberFormat;
import java.util.Scanner;

/**
 *
 * @author Samhith
 */
public class Discount {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        // Constants
        
        final double discount = 0.1;
        Scanner input = new Scanner(System.in);
        NumberFormat money = NumberFormat.getCurrencyInstance();
        
        // Variables
        
        double purchases, discountedPrice;
        boolean sale = false;
        
        // Input
        
        System.out.println("Enter amount of purchases: ");
        purchases = input.nextDouble();
        
        // Processing
        
        if (purchases >= 10) {
            
            discountedPrice = purchases - purchases * discount;
            sale = true;
            
        } else {
            
            discountedPrice = 0;
            sale = false;
            
        }
        
        // Output
        
        if (sale) {
            
            System.out.println("Discounted Price: " + money.format(discountedPrice));
            
        } else {
            
            System.out.println("Discounted Price: NO DISCOUNT \nFinal Price: " + money.format(purchases));
            
        }
        
        
    }
    
}
