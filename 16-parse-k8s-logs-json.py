import json

log_dict = {}
log_list = []


def parse(input_file):
    with open(input_file, "r") as file:
        for line in file:
            j = json.loads(line)
            log_dict["timestamp"] = j["log"]["timestamp"]
            log_dict["message"] = j["log"]["message"]
            log_dict["namespace"] = j["log"]["kubernetes"]["namespace_labels"][
                "kubernetes.io/metadata.name"
            ]
            log_dict["pod_name"] = j["log"]["kubernetes"]["pod_name"]
            log_dict["container_name"] = j["log"]["kubernetes"]["container_name"]
            log_dict["pod_ip"] = j["log"]["kubernetes"]["pod_ip"]
            log_dict["node_name"] = j["log"]["kubernetes"]["pod_node_name"]
            print(log_dict)
            log_list.append(log_dict)

        return log_list


parse(input_file="log.json")
