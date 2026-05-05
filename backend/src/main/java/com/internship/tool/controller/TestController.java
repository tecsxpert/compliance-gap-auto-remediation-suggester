package com.internship.tool.controller;

import com.internship.tool.service.ComplianceService;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/compliance")
public class TestController {

    private final ComplianceService complianceService;

    public TestController(ComplianceService complianceService) {
        this.complianceService = complianceService;
    }

    @PostMapping("/analyze")
    public String analyze(@RequestBody Map<String, Object> data) {
        return complianceService.create(data);
    }

    @PostMapping("/recommend")
    public String recommend(@RequestBody Map<String, Object> data) {
        return complianceService.getRecommendations(data);
    }

    @PostMapping("/report")
    public String report(@RequestBody Map<String, Object> data) {
        return complianceService.getReport(data);
    }
}