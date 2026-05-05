package com.internship.tool.service;


import org.springframework.stereotype.Service;

import java.util.Map;

@Service
public class ComplianceService {

    private final AiServiceClient aiServiceClient;

    public ComplianceService(AiServiceClient aiServiceClient) {
        this.aiServiceClient = aiServiceClient;
    }

    // Main method called from controller
    public String create(Map<String, Object> data) {
        // Call AI and return response directly
        return enrichWithAi(data);
    }

    public String getRecommendations(Map<String, Object> data) {
        return aiServiceClient.recommend(data);
    }

    public String getReport(Map<String, Object> data) {
        return aiServiceClient.generateReport(data);
    }

    // Async method 
    public String enrichWithAi(Map<String, Object> data) {
        try {
            String result = aiServiceClient.describe(data);

            if (result != null) {
                return result;
            } else {
                return "AI returned null response";
            }

        } catch (Exception e) {
            return "AI call failed: " + e.getMessage();
        }
    }
}