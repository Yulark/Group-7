/* Dashboard JavaScript */

let testScenarios = [];

document.addEventListener('DOMContentLoaded', () => {
    loadUserInfo();
    setupMenuLinks();
    loadTestScenarios();
    setupLogout();
    loadAccessSummary();
    setupSecurityFeatures();
});

// Setup advanced security features
function setupSecurityFeatures() {
    // Load security data when Security menu is clicked
    document.addEventListener('click', (e) => {
        if (e.target.textContent.includes('Security')) {
            setTimeout(() => {
                loadRiskAssessment();
                loadBehavioralAnalysis();
                loadComplianceStatus();
                loadDeviceSecurity();
                loadThreatDetection();
                loadRateLimitStatus();
            }, 100);
        }
    });
    
    // Setup security action buttons
    document.getElementById('initiateMfa')?.addEventListener('click', initiateMFA);
    document.getElementById('requestElevatedAccess')?.addEventListener('click', requestElevatedAccess);
    document.getElementById('verifyDevice')?.addEventListener('click', verifyDevice);
    
    // Load security data on initial page load
    setTimeout(() => {
        loadRiskAssessment();
        loadBehavioralAnalysis();
        loadComplianceStatus();
        loadDeviceSecurity();
        loadThreatDetection();
        loadRateLimitStatus();
    }, 500);
}

// Load user information
async function loadUserInfo() {
    try {
        const response = await fetch('/api/user-info');
        if (response.ok) {
            const data = await response.json();
            updateUserDisplay(data);
        }
    } catch (error) {
        console.error('Error loading user info:', error);
    }
}

function updateUserDisplay(data) {
    // Update stats
    document.getElementById('lastLogin').textContent = data.last_login;
    document.getElementById('deviceStatus').textContent = data.device_secure ? '✓ Secure' : '✗ Not Secure';
    document.getElementById('deviceSecure').textContent = data.device_secure ? '✓ Secure' : '✗ Not Secure';
    document.getElementById('permissionCount').textContent = data.permissions.length;

    // Update permissions
    const permList = document.getElementById('permissionsList');
    permList.innerHTML = data.permissions.map(p => `<li>${p}</li>`).join('');

    // Update DRM permissions
    const drmList = document.getElementById('drmPermissionsList');
    drmList.innerHTML = data.drm_permissions.map(p => `<li>${p}</li>`).join('');
}

// Setup menu links
function setupMenuLinks() {
    const menuLinks = document.querySelectorAll('.menu-link');
    menuLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Remove active class from all links
            menuLinks.forEach(l => l.classList.remove('active'));
            // Add active class to clicked link
            link.classList.add('active');

            // Hide all sections
            document.querySelectorAll('.section-content').forEach(section => {
                section.classList.add('hidden');
            });

            // Show selected section
            const targetId = link.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.classList.remove('hidden');
            }
        });
    });

    // Set first link as active
    if (menuLinks.length > 0) {
        menuLinks[0].classList.add('active');
    }
}

// Load test scenarios
async function loadTestScenarios() {
    try {
        const response = await fetch('/api/test-scenarios');
        if (response.ok) {
            const data = await response.json();
            testScenarios = data.scenarios;
            renderScenarios();
        }
    } catch (error) {
        console.error('Error loading test scenarios:', error);
    }
}

function renderScenarios() {
    const container = document.getElementById('scenariosList');
    container.innerHTML = testScenarios.map(scenario => `
        <button class="scenario-btn" data-scenario-id="${scenario.id}" onclick="runScenario(${scenario.id})">
            <div class="scenario-title">${scenario.name}</div>
            <div class="scenario-desc">${scenario.description}</div>
        </button>
    `).join('');
}

// Run test scenario
async function runScenario(scenarioId) {
    try {
        // Update UI to show selected scenario
        document.querySelectorAll('.scenario-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelector(`[data-scenario-id="${scenarioId}"]`).classList.add('active');

        // Show loading state
        const resultsDiv = document.getElementById('testResults');
        resultsDiv.innerHTML = '<p>Running test...</p>';

        // Call API
        const response = await fetch(`/api/run-test/${scenarioId}`, {
            method: 'POST'
        });

        if (response.ok) {
            const data = await response.json();
            displayTestResult(data);
        } else {
            resultsDiv.innerHTML = '<p class="error">Error running test</p>';
        }
    } catch (error) {
        console.error('Error running test:', error);
        document.getElementById('testResults').innerHTML = '<p class="error">Error running test</p>';
    }
}

function displayTestResult(data) {
    const resultsDiv = document.getElementById('testResults');
    const result = data.test_result;
    
    const resultStatus = result.status === 'GRANTED' ? 'granted' : 'denied';
    
    resultsDiv.innerHTML = `
        <div class="test-result">
            <div class="result-status ${resultStatus}">
                ${result.status === 'GRANTED' ? '✓ GRANTED' : '✗ DENIED'}
            </div>
            <div class="result-detail">
                <strong>User:</strong> ${data.user}
            </div>
            <div class="result-detail">
                <strong>Role:</strong> ${data.role}
            </div>
            <div class="result-detail">
                <strong>Message:</strong> ${result.message}
            </div>
            <div class="result-detail">
                <strong>Timestamp:</strong> ${data.timestamp}
            </div>
        </div>
    `;
}

// Setup logout
function setupLogout() {
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async () => {
            try {
                await fetch('/api/logout', { method: 'POST' });
                window.location.href = '/';
            } catch (error) {
                console.error('Logout error:', error);
            }
        });
    }
}

// Load access summary
async function loadAccessSummary() {
    try {
        const response = await fetch('/api/access-summary');
        if (response.ok) {
            const data = await response.json();
            const summaryDiv = document.getElementById('accessSummary');
            summaryDiv.innerHTML = `
                <ul>
                    <li>Total Denied Attempts: ${data.summary.total_denied}</li>
                    <li>Generated: ${data.summary.timestamp}</li>
                    <li>System Status: Active</li>
                    <li>Security Level: High</li>
                </ul>
            `;
        }
    } catch (error) {
        console.error('Error loading access summary:', error);
    }
}

// Add animations to elements
window.addEventListener('load', () => {
    const elements = document.querySelectorAll('.stat-card, .permission-card, .report-card');
    elements.forEach((el, index) => {
        el.style.animation = `slideUp 0.6s ease-out ${index * 0.1}s backwards`;
    });
});

// ============================================================
// ADVANCED SECURITY FUNCTIONS
// ============================================================

// Load Risk Assessment
async function loadRiskAssessment() {
    try {
        const response = await fetch('/api/security/risk-assessment');
        if (response.ok) {
            const data = await response.json();
            const assessment = data.risk_assessment;
            const riskDiv = document.getElementById('riskAssessment');
            
            const riskColor = assessment.level === 'LOW' ? '#27ae60' : 
                            assessment.level === 'MEDIUM' ? '#f39c12' :
                            assessment.level === 'HIGH' ? '#e74c3c' : '#c0392b';
            
            riskDiv.innerHTML = `
                <div style="border-left: 4px solid ${riskColor}; padding-left: 15px;">
                    <p><strong>Risk Score:</strong> ${assessment.score}/100</p>
                    <p><strong>Risk Level:</strong> <span style="color: ${riskColor}; font-weight: bold;">${assessment.level}</span></p>
                    <p><strong>Failed Logins:</strong> ${assessment.factors.failed_login_attempts}</p>
                    <p><strong>Device:</strong> ${assessment.factors.device_security}</p>
                </div>
            `;
        }
    } catch (error) {
        console.error('Error loading risk assessment:', error);
    }
}

// Load Behavioral Analysis
async function loadBehavioralAnalysis() {
    try {
        const response = await fetch('/api/security/behavioral-analysis');
        if (response.ok) {
            const data = await response.json();
            const analysis = data.behavioral_analysis;
            const behaviorDiv = document.getElementById('behaviorAnalysis');
            
            const anomalies = analysis.current_activity_anomalies;
            const anomalyText = anomalies.length === 0 ? 'No anomalies detected' : anomalies.join(', ');
            
            behaviorDiv.innerHTML = `
                <p><strong>Current Anomalies:</strong> ${anomalies.length}</p>
                <p><strong>Details:</strong> ${anomalyText}</p>
                <p><strong>Risk Level:</strong> ${analysis.risk_level}</p>
            `;
        }
    } catch (error) {
        console.error('Error loading behavioral analysis:', error);
    }
}

// Load Compliance Status
async function loadComplianceStatus() {
    try {
        const response = await fetch('/api/security/compliance-status');
        if (response.ok) {
            const data = await response.json();
            const compliance = data.compliance;
            const complianceDiv = document.getElementById('complianceStatus');
            
            const violationText = compliance.violations.length === 0 ? '✓ Compliant' : 
                                compliance.violations.join(', ');
            
            complianceDiv.innerHTML = `
                <p><strong>Status:</strong> ${compliance.is_compliant ? '✅ Compliant' : '❌ Non-Compliant'}</p>
                <p><strong>Violations:</strong> ${compliance.violation_count}</p>
                <p><strong>Details:</strong> ${violationText}</p>
            `;
        }
    } catch (error) {
        console.error('Error loading compliance status:', error);
    }
}

// Load Device Security
async function loadDeviceSecurity() {
    try {
        const response = await fetch('/api/security/device-fingerprint', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_agent: navigator.userAgent })
        });
        if (response.ok) {
            const data = await response.json();
            const fingerprint = data.device_fingerprint;
            const deviceDiv = document.getElementById('deviceSecurity');
            
            deviceDiv.innerHTML = `
                <p><strong>Fingerprint:</strong> ${fingerprint.fingerprint_hash}</p>
                <p><strong>Integrity:</strong> ${fingerprint.integrity_valid ? '✅ Valid' : '❌ Invalid'}</p>
                <p><strong>Encryption:</strong> ${fingerprint.encryption_enabled ? '✅ Enabled' : '❌ Disabled'}</p>
                <p><strong>Malware:</strong> ${fingerprint.malware_detected ? '⚠️ Detected' : '✅ Clean'}</p>
                <p><strong>Security Score:</strong> ${fingerprint.security_score}/100</p>
            `;
        }
    } catch (error) {
        console.error('Error loading device security:', error);
    }
}

// Load Threat Detection
async function loadThreatDetection() {
    try {
        const response = await fetch('/api/security/threat-detection');
        if (response.ok) {
            const data = await response.json();
            const threats = data.threat_detection;
            const threatDiv = document.getElementById('threatDetection');
            
            threatDiv.innerHTML = `
                <p><strong>Monitoring:</strong> ${threats.monitoring_status}</p>
                <p><strong>Threats Blocked:</strong> ${threats.threats_blocked}</p>
                <p><strong>Threat Level:</strong> 🟢 ${threats.threat_level}</p>
                <p><strong>Last Check:</strong> Now</p>
            `;
        }
    } catch (error) {
        console.error('Error loading threat detection:', error);
    }
}

// Load Rate Limit Status
async function loadRateLimitStatus() {
    try {
        const response = await fetch('/api/security/rate-limit-status');
        if (response.ok) {
            const data = await response.json();
            const rateLimit = data.rate_limiting;
            const rateLimitDiv = document.getElementById('rateLimitStatus');
            
            rateLimitDiv.innerHTML = `
                <p><strong>Requests/Hour:</strong> ${rateLimit.requests_this_hour}/${rateLimit.limit}</p>
                <p><strong>Remaining:</strong> ${rateLimit.remaining}</p>
                <p><strong>Reset in:</strong> ${rateLimit.reset_time}</p>
                <p><strong>Status:</strong> ${rateLimit.blocked ? '🔴 Blocked' : '🟢 Active'}</p>
            `;
        }
    } catch (error) {
        console.error('Error loading rate limit status:', error);
    }
}

// Initiate MFA
async function initiateMFA() {
    try {
        const response = await fetch('/api/security/mfa/initiate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ type: 'EMAIL' })
        });
        if (response.ok) {
            const data = await response.json();
            alert('MFA challenge sent via ' + data.mfa.type + '. Check your email.');
            
            // Prompt for token
            const token = prompt('Enter the 6-digit code sent to your email:');
            if (token) {
                const verifyResponse = await fetch('/api/security/mfa/verify', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ token: token })
                });
                if (verifyResponse.ok) {
                    alert('MFA verification successful!');
                }
            }
        }
    } catch (error) {
        console.error('Error initiating MFA:', error);
        alert('Error initiating MFA');
    }
}

// Request Elevated Access
async function requestElevatedAccess() {
    const resource = prompt('Enter resource name:') || 'CRITICAL_RESOURCE';
    const action = prompt('Enter action (VIEW/EDIT/DELETE/PUBLISH):') || 'EDIT';
    const justification = prompt('Provide justification for elevated access:') || 'Business critical need';
    
    try {
        const response = await fetch('/api/security/elevated-access', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                resource: resource,
                action: action,
                justification: justification
            })
        });
        if (response.ok) {
            const data = await response.json();
            alert('Request submitted with ID: ' + data.elevated_access.request_id + '\nStatus: ' + data.elevated_access.status);
        }
    } catch (error) {
        console.error('Error requesting elevated access:', error);
    }
}

// Verify Device
async function verifyDevice() {
    try {
        const response = await fetch('/api/security/device-fingerprint', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_agent: navigator.userAgent })
        });
        if (response.ok) {
            const data = await response.json();
            const fingerprint = data.device_fingerprint;
            alert(
                'Device Verification:\n' +
                'Fingerprint: ' + fingerprint.fingerprint_hash + '\n' +
                'Integrity: ' + (fingerprint.integrity_valid ? 'Valid' : 'Invalid') + '\n' +
                'Encryption: ' + (fingerprint.encryption_enabled ? 'Enabled' : 'Disabled') + '\n' +
                'Security Score: ' + fingerprint.security_score + '/100'
            );
        }
    } catch (error) {
        console.error('Error verifying device:', error);
    }
}

console.log('Dashboard script loaded with advanced security features');
