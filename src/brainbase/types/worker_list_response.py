# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WorkerListResponse",
    "WorkerListResponseItem",
    "WorkerListResponseItemDeployments",
    "WorkerListResponseItemDeploymentsFlow",
    "WorkerListResponseItemDeploymentsHistory",
    "WorkerListResponseItemDeploymentsDelegateAuxChatDeployment",
    "WorkerListResponseItemDeploymentsDelegateAuxEmailDeployment",
    "WorkerListResponseItemDeploymentsDelegateAuxSlackDeployment",
    "WorkerListResponseItemDeploymentsDelegateAuxSMsDeployment",
    "WorkerListResponseItemDeploymentsDelegateAuxVoiceDeployment",
    "WorkerListResponseItemFlows",
    "WorkerListResponseItemFlowsDeployments",
    "WorkerListResponseItemFlowsDeploymentsHistory",
    "WorkerListResponseItemFlowsDeploymentsDelegateAuxChatDeployment",
    "WorkerListResponseItemFlowsDeploymentsDelegateAuxEmailDeployment",
    "WorkerListResponseItemFlowsDeploymentsDelegateAuxSlackDeployment",
    "WorkerListResponseItemFlowsDeploymentsDelegateAuxSMsDeployment",
    "WorkerListResponseItemFlowsDeploymentsDelegateAuxVoiceDeployment",
    "WorkerListResponseItemIntegrations",
    "WorkerListResponseItemIntegrationsTeam",
    "WorkerListResponseItemIntegrationsTeamAPIKeys",
    "WorkerListResponseItemIntegrationsTeamUsers",
    "WorkerListResponseItemIntegrationsTeamUsersUser",
    "WorkerListResponseItemIntegrationsTeamUsersUserIdentities",
    "WorkerListResponseItemResources",
    "WorkerListResponseItemResourcesDelegateAuxDatabaseResource",
    "WorkerListResponseItemResourcesDelegateAuxRAgResource",
    "WorkerListResponseItemTeam",
    "WorkerListResponseItemTeamAPIKeys",
    "WorkerListResponseItemTeamIntegrations",
    "WorkerListResponseItemTeamUsers",
    "WorkerListResponseItemTeamUsersUser",
    "WorkerListResponseItemTeamUsersUserIdentities",
]


class WorkerListResponseItemDeploymentsFlow(BaseModel):
    id: str

    code: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version: int

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    label: Optional[str] = None


class WorkerListResponseItemDeploymentsHistory(BaseModel):
    id: str

    deployed_at: datetime = FieldInfo(alias="deployedAt")

    deployment: object

    deployment_id: str = FieldInfo(alias="deploymentId")

    flow_version: int = FieldInfo(alias="flowVersion")

    status: str

    metadata: Optional[object] = None


class WorkerListResponseItemDeploymentsDelegateAuxChatDeployment(BaseModel):
    id: str

    allowed_users: str = FieldInfo(alias="allowedUsers")

    delegate_aux_deployments: object

    api_model_config: object = FieldInfo(alias="modelConfig")

    llm_model: Optional[str] = FieldInfo(alias="llmModel", default=None)

    welcome_message: Optional[str] = FieldInfo(alias="welcomeMessage", default=None)


class WorkerListResponseItemDeploymentsDelegateAuxEmailDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    email_template: Optional[str] = FieldInfo(alias="emailTemplate", default=None)

    from_email: Optional[str] = FieldInfo(alias="fromEmail", default=None)

    subject: Optional[str] = None


class WorkerListResponseItemDeploymentsDelegateAuxSlackDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    bot_token: Optional[str] = FieldInfo(alias="botToken", default=None)

    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)


class WorkerListResponseItemDeploymentsDelegateAuxSMsDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    sms_provider: Optional[str] = FieldInfo(alias="smsProvider", default=None)


class WorkerListResponseItemDeploymentsDelegateAuxVoiceDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    voice_id: Optional[str] = FieldInfo(alias="voiceId", default=None)

    voice_provider: Optional[str] = FieldInfo(alias="voiceProvider", default=None)


class WorkerListResponseItemDeployments(BaseModel):
    id: str

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    flow: WorkerListResponseItemDeploymentsFlow

    flow_id: str = FieldInfo(alias="flowId")

    history: WorkerListResponseItemDeploymentsHistory

    name: str

    status: str

    type: object

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_chat_deployment: Optional[WorkerListResponseItemDeploymentsDelegateAuxChatDeployment] = FieldInfo(
        alias="delegate_aux_chatDeployment", default=None
    )

    delegate_aux_email_deployment: Optional[WorkerListResponseItemDeploymentsDelegateAuxEmailDeployment] = FieldInfo(
        alias="delegate_aux_emailDeployment", default=None
    )

    delegate_aux_slack_deployment: Optional[WorkerListResponseItemDeploymentsDelegateAuxSlackDeployment] = FieldInfo(
        alias="delegate_aux_slackDeployment", default=None
    )

    delegate_aux_s_ms_deployment: Optional[WorkerListResponseItemDeploymentsDelegateAuxSMsDeployment] = FieldInfo(
        alias="delegate_aux_sMSDeployment", default=None
    )

    delegate_aux_voice_deployment: Optional[WorkerListResponseItemDeploymentsDelegateAuxVoiceDeployment] = FieldInfo(
        alias="delegate_aux_voiceDeployment", default=None
    )


class WorkerListResponseItemFlowsDeploymentsHistory(BaseModel):
    id: str

    deployed_at: datetime = FieldInfo(alias="deployedAt")

    deployment: object

    deployment_id: str = FieldInfo(alias="deploymentId")

    flow_version: int = FieldInfo(alias="flowVersion")

    status: str

    metadata: Optional[object] = None


class WorkerListResponseItemFlowsDeploymentsDelegateAuxChatDeployment(BaseModel):
    id: str

    allowed_users: str = FieldInfo(alias="allowedUsers")

    delegate_aux_deployments: object

    api_model_config: object = FieldInfo(alias="modelConfig")

    llm_model: Optional[str] = FieldInfo(alias="llmModel", default=None)

    welcome_message: Optional[str] = FieldInfo(alias="welcomeMessage", default=None)


class WorkerListResponseItemFlowsDeploymentsDelegateAuxEmailDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    email_template: Optional[str] = FieldInfo(alias="emailTemplate", default=None)

    from_email: Optional[str] = FieldInfo(alias="fromEmail", default=None)

    subject: Optional[str] = None


class WorkerListResponseItemFlowsDeploymentsDelegateAuxSlackDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    bot_token: Optional[str] = FieldInfo(alias="botToken", default=None)

    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)


class WorkerListResponseItemFlowsDeploymentsDelegateAuxSMsDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    sms_provider: Optional[str] = FieldInfo(alias="smsProvider", default=None)


class WorkerListResponseItemFlowsDeploymentsDelegateAuxVoiceDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    voice_id: Optional[str] = FieldInfo(alias="voiceId", default=None)

    voice_provider: Optional[str] = FieldInfo(alias="voiceProvider", default=None)


class WorkerListResponseItemFlowsDeployments(BaseModel):
    id: str

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    flow: object

    flow_id: str = FieldInfo(alias="flowId")

    history: WorkerListResponseItemFlowsDeploymentsHistory

    name: str

    status: str

    type: object

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_chat_deployment: Optional[WorkerListResponseItemFlowsDeploymentsDelegateAuxChatDeployment] = FieldInfo(
        alias="delegate_aux_chatDeployment", default=None
    )

    delegate_aux_email_deployment: Optional[WorkerListResponseItemFlowsDeploymentsDelegateAuxEmailDeployment] = (
        FieldInfo(alias="delegate_aux_emailDeployment", default=None)
    )

    delegate_aux_slack_deployment: Optional[WorkerListResponseItemFlowsDeploymentsDelegateAuxSlackDeployment] = (
        FieldInfo(alias="delegate_aux_slackDeployment", default=None)
    )

    delegate_aux_s_ms_deployment: Optional[WorkerListResponseItemFlowsDeploymentsDelegateAuxSMsDeployment] = FieldInfo(
        alias="delegate_aux_sMSDeployment", default=None
    )

    delegate_aux_voice_deployment: Optional[WorkerListResponseItemFlowsDeploymentsDelegateAuxVoiceDeployment] = (
        FieldInfo(alias="delegate_aux_voiceDeployment", default=None)
    )


class WorkerListResponseItemFlows(BaseModel):
    id: str

    code: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: WorkerListResponseItemFlowsDeployments

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version: int

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    label: Optional[str] = None


class WorkerListResponseItemIntegrationsTeamAPIKeys(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    is_active: bool = FieldInfo(alias="isActive")

    key_hash: str = FieldInfo(alias="keyHash")

    name: str

    scopes: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    truncated_key: str = FieldInfo(alias="truncatedKey")

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)


class WorkerListResponseItemIntegrationsTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class WorkerListResponseItemIntegrationsTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: WorkerListResponseItemIntegrationsTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class WorkerListResponseItemIntegrationsTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: WorkerListResponseItemIntegrationsTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class WorkerListResponseItemIntegrationsTeam(BaseModel):
    id: str

    api_keys: WorkerListResponseItemIntegrationsTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: WorkerListResponseItemIntegrationsTeamUsers

    workers: object


class WorkerListResponseItemIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[WorkerListResponseItemIntegrationsTeam] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class WorkerListResponseItemResourcesDelegateAuxDatabaseResource(BaseModel):
    id: str

    database_name: str = FieldInfo(alias="databaseName")

    delegate_aux_resources: object

    host: str

    password: str

    port: int

    username: str

    connection_string: Optional[str] = FieldInfo(alias="connectionString", default=None)


class WorkerListResponseItemResourcesDelegateAuxRAgResource(BaseModel):
    id: str

    delegate_aux_resources: object

    rag_type: object = FieldInfo(alias="ragType")

    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)

    image_s3_file_path: Optional[str] = FieldInfo(alias="imageS3FilePath", default=None)

    key: Optional[str] = None

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)

    num_scrolls: Optional[int] = FieldInfo(alias="numScrolls", default=None)

    raw_link: Optional[str] = FieldInfo(alias="rawLink", default=None)

    s3_file_path: Optional[str] = FieldInfo(alias="s3FilePath", default=None)

    signed_s3_file_path: Optional[str] = FieldInfo(alias="signedS3FilePath", default=None)

    size: Optional[int] = None

    status: Optional[str] = None

    update_frequency: Optional[str] = FieldInfo(alias="updateFrequency", default=None)

    uploaded_at: Optional[datetime] = FieldInfo(alias="uploadedAt", default=None)


class WorkerListResponseItemResources(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    resource_type: object = FieldInfo(alias="resourceType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_database_resource: Optional[WorkerListResponseItemResourcesDelegateAuxDatabaseResource] = FieldInfo(
        alias="delegate_aux_databaseResource", default=None
    )

    delegate_aux_r_ag_resource: Optional[WorkerListResponseItemResourcesDelegateAuxRAgResource] = FieldInfo(
        alias="delegate_aux_rAGResource", default=None
    )


class WorkerListResponseItemTeamAPIKeys(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    is_active: bool = FieldInfo(alias="isActive")

    key_hash: str = FieldInfo(alias="keyHash")

    name: str

    scopes: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    truncated_key: str = FieldInfo(alias="truncatedKey")

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)


class WorkerListResponseItemTeamIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[object] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class WorkerListResponseItemTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class WorkerListResponseItemTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: WorkerListResponseItemTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class WorkerListResponseItemTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: WorkerListResponseItemTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class WorkerListResponseItemTeam(BaseModel):
    id: str

    api_keys: WorkerListResponseItemTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: WorkerListResponseItemTeamIntegrations

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: WorkerListResponseItemTeamUsers

    workers: object


class WorkerListResponseItem(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: WorkerListResponseItemDeployments

    flows: WorkerListResponseItemFlows

    integrations: WorkerListResponseItemIntegrations

    name: str

    resources: WorkerListResponseItemResources

    team: WorkerListResponseItemTeam

    team_id: str = FieldInfo(alias="teamId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None

    last_refreshed_at: Optional[datetime] = FieldInfo(alias="lastRefreshedAt", default=None)

    status: Optional[str] = None


WorkerListResponse: TypeAlias = List[WorkerListResponseItem]
