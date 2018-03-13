//
//  ViewController.swift
//  Downloading Web Content
//
//  Created by Samhith Sripada on 2018-01-03.
//  Copyright © 2018 HackedApple. All rights reserved.
//

import UIKit
import WebKit

class ViewController: UIViewController {

    @IBOutlet var webView: WKWebView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        
        // let url = URL(string: "https://www.apple.com/ca")!
        
        // webView.load(URLRequest(url: url))
        
        // webView.loadHTMLString("<h1>Hello There!</h1>", baseURL: nil)
        
        if let url = URL(string: "https://www.apple.com") {
        
            let request = NSMutableURLRequest(url: url)
            
            let task = 
    
        }
        
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

