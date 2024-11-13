# Copyright 2024 The DLRover Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dlrover.python.diagnosis.inferencechain.inferenceoperator.observer.check_failure_node_operator import (  # noqa: E501
    CheckFailureNodeOperator,
)
from dlrover.python.diagnosis.inferencechain.inferenceoperator.observer.check_training_hang_operator import (  # noqa: E501
    CheckTrainingHangOperator,
)
from dlrover.python.diagnosis.inferencechain.inferenceoperator.observer.metrics_collection_operator import (  # noqa: E501
    MetricsCollectionOperator,
)
from dlrover.python.diagnosis.inferencechain.inferenceoperator.resolver.resolve_training_hang_operator import (  # noqa: E501
    ResolveTrainingHangOperator,
)
from dlrover.python.master.diagnosis.diagnosis_data_manager import (
    DiagnosisDataManager,
)


def get_training_failure_operators():
    return [CheckFailureNodeOperator()]


def get_worker_observe_operators():
    return [MetricsCollectionOperator()]


def get_worker_diagnosis_operators():
    return []


def get_master_observing_operators(data_mgr: DiagnosisDataManager = None):
    return [
        CheckTrainingHangOperator(data_mgr),
    ]


def get_master_observer_operators(data_mgr: DiagnosisDataManager = None):
    return [
        CheckTrainingHangOperator(data_mgr),
    ]


def get_master_resolver_operators(data_mgr: DiagnosisDataManager = None):
    return [
        ResolveTrainingHangOperator(data_mgr),
    ]
