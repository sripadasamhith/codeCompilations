/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.hdsb.gwss.sripada_sam.ics3u.u2;

import java.util.Scanner;

/**
 *
 * @author 1sripadasam
 */
public class RectangleAreaCalculator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here

        // VARIABLES
        
        double length, width, area;

        // OBJECTS
        
        Scanner input = new Scanner(System.in);
        
        
        
        // INTRO
        
        System.out.println("THIS PROGRAM ASKS THE USER FOR..");

        // INPUT
        
        System.out.println("PLEASE ENTER THE LENGTH: ");
        
        length = input.nextDouble();
        
        System.out.println("PLEASE ENTER THE WIDTH: ");
        
        width = input.nextDouble();
        
        // PROCESSING
        
        area = length * width;
        
        // OUTPUT
        
        System.out.println("THE ARE OF THE RECTANGLE IS " + area + " units^2.");
    }

}
