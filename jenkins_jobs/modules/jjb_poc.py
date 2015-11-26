import xml.etree.ElementTree as ET
import yaml

properties = [
    {
        "yaml": "properties",
        "xml": "properties",
        "fields":
            [
                {
                    "yaml": "builds-chain-fingerprinter",
                    "xml": "org.jenkinsci.plugins."
                           "buildschainfingerprinter."
                           "AutomaticFingerprintJobProperty",
                    "fields": 
                        [
                            {
                                "yaml": "per-builds-chain",
                                "xml": "isPerBuildsChainEnabled",
                                "default": "false"
                            },
                            {
                                "yaml": "per-job-chain",
                                "xml": "isPerJobsChainEnabled",
                                "default": "false"
                             }
                        ]
                },
                {
                    "yaml": "ownership",
                    "xml": "com.synopsys.arc.jenkins.plugins."
                           "ownership.jobs.JobOwnerJobProperty",
                    "fields": 
                        [
                            {
                                "yaml": "",
                                "xml": "ownership",
                                "fields": 
                                    [
                                        {
                                            "yaml": "enabled",
                                            "xml": "ownershipEnabled",
                                            "default": "true"
                                        },
                                        {
                                            "yaml": "owner",
                                            "xml": "primaryOwnerId"
                                        },
                                        {
                                            "yaml": "co-owners",
                                            "xml": "coownersIds",
                                            "multiple": "string",
                                            "default": []
                                        }
                                    ]
                            }
                        ]
                },
                {
                    "yaml": "promoted-build",
                    "xml": "hudson.plugins.promoted__builds."
                           "JobPropertyImpl",
                    "fields":
                        [
                            {
                                "yaml": "names",
                                "xml": "activeProcessNames",
                                "multiple": "string",
                                "default": []
                            }
                        ]
                },
                {
                    "yaml": "github",
                    "xml":  "GithubProjectProperty",
                    "fields":
                        [
                            {
                                "yaml": "url",
                                "xml": "projectUrl"
                            }
                        ]
                },
                {
                    "yaml": "least-load",
                    "xml": "org.bstick12.jenkinsci.plugins.leastload."
                           "LeastLoadDisabledProperty",
                    "fields":
                        [
                            {
                                "yaml": "disabled",
                                "xml": "leastLoadDisabled",
                                "default": "true"
                            }
                        ]
                },
                {
                    "yaml": "throttle",
                    "xml": "hudson.plugins.throttleconcurrents."
                           "ThrottleJobProperty",
                    "fields": 
                        [
                            {
                                "yaml": "max-per-node",
                                "xml": "maxConcurrentPerNode",
                                "default": 0
                            },
                            {
                                "yaml": "max-total",
                                "xml": "maxConcurrentTotal",
                                "default": 0
                            },
                            {
                                "yaml": "enabled",
                                "xml": "throttleEnabled",
                                "default": "true"
                            },
                            {
                                "yaml": "categories",
                                "xml": "categories",
                                "multiple": "string",
                                "default": []
                            },
                            {
                                "yaml": "option",
                                "xml": "throttleOption",
                            },
                            {
                                "reverseyaml": "",
                                "xml": "configVersion",
                                "default": "1"
                            }
                        ]
                },
                {
                  "yaml": "sidebar",
                  "xml": "hudson.plugins.sidebar__link.ProjectLinks",
                  "no_yaml": True,
                  "fields" : 
                    [
                        {
                            "yaml": "",
                            "xml": "links",
                            "fields":
                                [
                                    {
                                        "yaml": "sidebar",
                                        "xml": "hudson.plugins."
                                                    "sidebar__link."
                                                    "LinkAction",
                                        "fields":
                                            [
                                                {
                                                    "yaml": "url",
                                                    "xml": "url",
                                                },
                                                {
                                                    "yaml": "text",
                                                    "xml": "text",
                                                },
                                                {
                                                    "yaml": "icon",
                                                    "xml": "icon",
                                                }
                                            ]
                                    }
                                ]
                        } 
                    ]
                },
                {
                    "yaml": "inject",
                    "xml": "EnvInjectJobProperty",
                    "fields":
                        [
                            {
                                "yaml": "",
                                "xml": "info",
                                "fields":
                                    [
                                        {
                                            "yaml": "properties-file",
                                            "xml": "propertiesFilePath"
                                        },
                                        {
                                            "yaml": "properties-content",
                                            "xml": "propertiesContent"
                                        },
                                        {
                                            "yaml": "script-file",
                                            "xml": "scriptFilePath"
                                        },
                                        {
                                            "yaml": "script-content",
                                            "xml": "scriptContent"
                                        },
                                        {
                                            "yaml": "groovy-content",
                                            "xml": "groovyScriptContent"
                                        },
                                        {
                                            "yaml": "load-from-master",
                                            "xml": "loadFilesFromMaster",
                                            "default": "false"
                                        }
                                    ]
                            },
                            {
                                "yaml": "enabled",
                                "xml": "on",
                                "default": "true"
                            },
                            {
                                "yaml": "keep-system-variables",
                                "xml": "keepJenkinsSystemVariables",
                                "default": "true"
                            },
                            {
                                "yaml": "keep-build-variables",
                                "xml": "keepBuildVariables",
                                "default": "true"
                            },
                            {
                                "yaml": "override-build-parameters",
                                "xml": "overrideBuildParameters",
                                "default": "false"
                            }
                        ]
                },
# authenticated_build is deprecated
# NOT FINISHED AUTHORIZATION. COMPLICATED
                {
                    "yaml": "authorization",
                    "xml": "hudson.security.AuthorizationMatrixProperty",
                    "map_function": "authorization_map"
                },
# END AUTHORIZATION
# extended_choice is deprecated
                {
                    "yaml": "priority-sorter",
                    "xml": "hudson.queueSorter.PrioritySorterJobProperty",
                    "fields": [{"priority": "priority"}]
                },
                {
                    "yaml": "build-blocker",
                    "xml": "hudson.plugins."
                           "buildblocker.BuildBlockerProperty",
                    "fields" :
                        [
                            {
                                "yaml": "blocking-jobs",
                                "xml": "blockingJobs",
                                "aggregate": "\n",
                                "required": True
                            },
                            {
                                "yaml": "use-build-blocker",
                                "xml": "useBuildBlocker",
                                "default": "true"
                            }
                        ]
                },
                {
                    "yaml": "copyartifact",
                    "xml": "hudson.plugins.copyartifact."
                           "CopyArtifactPermissionProperty",
                    "plugin": "copyartifact",
                    "fields":
                        [
                            {
                                "yaml": "projects",
                                "xml": "projectNameList",
                                "multiple": "string",
                                "required": "true"
                            }
                        ]
                },
                {
                    "yaml": "batch-tasks",
                    "xml": "hudson.plugins.batch__task.BatchTaskProperty",
                    "fields":
                        [
                            {
                                "yaml": "",
                                "xml": "tasks",
                                "fields":
                                    [
                                        {
                                            "yaml": "",
                                            "xml": "hudson.plugins."
                                                        "batch__task."
                                                        "BatchTask",
                                            "fields":
                                                [
                                                    {
                                                        "yaml": "name",
                                                        "xml": "name"
                                                    },
                                                    {
                                                        "yaml": "script",
                                                        "xml": "script"
                                                    }
                                                ]
                                        }
                                    ]
                            }
                        ]
                },
                {
                    "yaml": "heavy-job",
                    "xml": "hudson.plugins.heavy__job.HeavyJobProperty",
                    "fields": [{reverse
                                "yaml": "weight",
                                "xml": "weight",
                                "default": 1
                              }]
                },
# FIGURE OUT HOW TO HANDLE MULTIPLE XML FIELDS FROM ONE YAML
                {
                    "yaml": "slave-utilization",
                    "xml": "com.suryagaddipati.jenkins."
                           "SlaveUtilizationProperty",
                    "fields":
                        [
                            {
                                "yaml": "slave-percentage",
                                "xml": "slaveUtilizationPercentage",
                                "default": 0,
                                "additional_xml": "needsExclusiveAccess"
                                                  "ToNode",
                                "additional_logic": 
                                    "'false' if not %s else 'true'"
                                    
                            },
                            {   
                                "yaml": "single-instance-per-slave",
                                "xml": "singleInstancePerSlave",
                                "default": "false"
                            }
                        ]
                },
                {
                    "yaml": "delivery-pipeline",
                    "xml": "se.diabol.jenkins.pipeline.PipelineProperty",
                    "fields":
                        [
                            {
                                "yaml": "stage",
                                "xml": "stageName",
                                "default": ""
                            },
                            {
                                "yaml": "task",
                                "xml": "taskName",
                                "default": ""
                            }
                        ]
                },
                {
                    "yaml": "zeromq-event",
                    "xml": "org.jenkinsci.plugins."
                           "ZMQEventPublisher.HudsonNotificationProperty",
                    "fields":
                        [
                            {
                                "yaml": "",
                                "xml": "enabled",
                                "value": "true"
                            }
                        ]
                }
            ]
     }
]

def parse_properties(node, props, indent=0):
    for items in props:
        newindent = indent
        if items.get("xml", None) == node.tag:
            if items.get("yaml", None):
                mult = items.get("multiple", None)
                if mult:
                    if not items.get("fields", None):
                        vals = []
                        for mul_child in node:
                            if mul_child.tag == mult:
                                vals.append(mul_child.text.strip())
                else:
                    vals = [node.text.strip() if node.text else ""]
                default_val = items.get("default", None)
                if ",".join(vals) != default_val and not \
                        items.get("no_yaml", False):
                    print "%s%s: %s" % ("\t"*indent, items["yaml"], ",".join(vals))
                    newindent = indent + 1
            if items.get("fields", None): 
                for child in node:
                    parse_properties(child, items["fields"], newindent)
    

#xml_file  = "/home/szacks/git/jenkins-job-builder/tests/properties/fixtures/copyartifact.xml"
#xml_file  = "/home/szacks/git/jenkins-job-builder/tests/properties/fixtures/ownership.xml"
xml_file = "/home/szacks/Documents/fulltest.xml"
with open(xml_file) as f:
    tree = ET.fromstring(f.read())

for toplevel in tree:
    parse_properties(toplevel, properties)        

