/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.hdsb.gwss.sripada_sam.ics3u.u3;

import java.util.Scanner;

/**
 *
 * @author Samhith
 */
public class AlienDetector {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Scanner input = new Scanner(System.in);
        
        int alienAntennas, alienEyes;
        
        System.out.println("How many antennas: ");
        alienAntennas = input.nextInt();
        
        System.out.println("How many eyes: ");
        alienEyes = input.nextInt();
        
        
        if (alienAntennas >= 3 && alienEyes <= 4) {
            
            System.out.println("TroyMartian");
            
        } else if (alienAntennas <= 6 && alienEyes >= 2) {
            
            System.out.println("VladSaturnian");
            
        } if (alienAntennas <= 2 && alienEyes <= 3) {
            
            System.out.println("GraemeMercurian");
            
        } else {
            
            System.out.println(" ");
            
        }
        
    }
    
}
