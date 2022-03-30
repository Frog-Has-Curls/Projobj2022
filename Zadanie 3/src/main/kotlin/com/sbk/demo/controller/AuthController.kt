package com.sbk.demo.controller

import com.sbk.demo.authService.AuthService
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.http.MediaType
import org.springframework.web.bind.annotation.*
import org.springframework.beans.factory.annotation.Autowired


import javax.servlet.http.HttpServletRequest
import javax.persistence.*

@RestController
class AuthController 
	@Autowired 
		lateinit var authService: AuthService

{
	@PostMapping("/login", produces = [MediaType.TEXT_PLAIN_VALUE]) 
	fun login(@RequestBody, log: String, @RequestBody  pass: String): HttpStatus {
		loginProviders.login(logi, password) 
	return HttpStatus.OK	
	}
	
	@GetMapping("/logout")
	fun logout(): ResponseEntity<String>{
		return ResponseEntity("Success", HttpStatus.OK)
		}
}