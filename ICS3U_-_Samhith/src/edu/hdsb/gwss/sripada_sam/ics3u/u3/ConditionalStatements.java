/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.hdsb.gwss.sripada_sam.ics3u.u3;

/**
 *
 * @author 1sripadasam
 */
public class ConditionalStatements {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        boolean thirtyCredits = true;
        boolean fortyHours = true;
        boolean litTest = true;
        
        if (thirtyCredits && fortyHours && litTest) {
            
            System.out.println("You graduate!!");
            
        } else {
            
            System.out.println("You failed!!!!");
            
        }
        
        
    }
    
}
