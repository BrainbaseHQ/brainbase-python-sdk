# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FlowListResponse",
    "FlowListResponseItem",
    "FlowListResponseItemDeployments",
    "FlowListResponseItemDeploymentsHistory",
    "FlowListResponseItemDeploymentsWorker",
    "FlowListResponseItemDeploymentsWorkerIntegrations",
    "FlowListResponseItemDeploymentsWorkerIntegrationsTeam",
    "FlowListResponseItemDeploymentsWorkerIntegrationsTeamAPIKeys",
    "FlowListResponseItemDeploymentsWorkerIntegrationsTeamUsers",
    "FlowListResponseItemDeploymentsWorkerIntegrationsTeamUsersUser",
    "FlowListResponseItemDeploymentsWorkerIntegrationsTeamUsersUserIdentities",
    "FlowListResponseItemDeploymentsWorkerResources",
    "FlowListResponseItemDeploymentsWorkerResourcesDelegateAuxDatabaseResource",
    "FlowListResponseItemDeploymentsWorkerResourcesDelegateAuxRAgResource",
    "FlowListResponseItemDeploymentsWorkerTeam",
    "FlowListResponseItemDeploymentsWorkerTeamAPIKeys",
    "FlowListResponseItemDeploymentsWorkerTeamIntegrations",
    "FlowListResponseItemDeploymentsWorkerTeamUsers",
    "FlowListResponseItemDeploymentsWorkerTeamUsersUser",
    "FlowListResponseItemDeploymentsWorkerTeamUsersUserIdentities",
    "FlowListResponseItemDeploymentsDelegateAuxChatDeployment",
    "FlowListResponseItemDeploymentsDelegateAuxEmailDeployment",
    "FlowListResponseItemDeploymentsDelegateAuxSlackDeployment",
    "FlowListResponseItemDeploymentsDelegateAuxSMsDeployment",
    "FlowListResponseItemDeploymentsDelegateAuxVoiceDeployment",
    "FlowListResponseItemWorker",
    "FlowListResponseItemWorkerDeployments",
    "FlowListResponseItemWorkerDeploymentsHistory",
    "FlowListResponseItemWorkerDeploymentsDelegateAuxChatDeployment",
    "FlowListResponseItemWorkerDeploymentsDelegateAuxEmailDeployment",
    "FlowListResponseItemWorkerDeploymentsDelegateAuxSlackDeployment",
    "FlowListResponseItemWorkerDeploymentsDelegateAuxSMsDeployment",
    "FlowListResponseItemWorkerDeploymentsDelegateAuxVoiceDeployment",
    "FlowListResponseItemWorkerIntegrations",
    "FlowListResponseItemWorkerIntegrationsTeam",
    "FlowListResponseItemWorkerIntegrationsTeamAPIKeys",
    "FlowListResponseItemWorkerIntegrationsTeamUsers",
    "FlowListResponseItemWorkerIntegrationsTeamUsersUser",
    "FlowListResponseItemWorkerIntegrationsTeamUsersUserIdentities",
    "FlowListResponseItemWorkerResources",
    "FlowListResponseItemWorkerResourcesDelegateAuxDatabaseResource",
    "FlowListResponseItemWorkerResourcesDelegateAuxRAgResource",
    "FlowListResponseItemWorkerTeam",
    "FlowListResponseItemWorkerTeamAPIKeys",
    "FlowListResponseItemWorkerTeamIntegrations",
    "FlowListResponseItemWorkerTeamUsers",
    "FlowListResponseItemWorkerTeamUsersUser",
    "FlowListResponseItemWorkerTeamUsersUserIdentities",
]


class FlowListResponseItemDeploymentsHistory(BaseModel):
    id: str

    deployed_at: datetime = FieldInfo(alias="deployedAt")

    deployment: object

    deployment_id: str = FieldInfo(alias="deploymentId")

    flow_version: int = FieldInfo(alias="flowVersion")

    status: str

    metadata: Optional[object] = None


class FlowListResponseItemDeploymentsWorkerIntegrationsTeamAPIKeys(BaseModel):
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


class FlowListResponseItemDeploymentsWorkerIntegrationsTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class FlowListResponseItemDeploymentsWorkerIntegrationsTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: FlowListResponseItemDeploymentsWorkerIntegrationsTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class FlowListResponseItemDeploymentsWorkerIntegrationsTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: FlowListResponseItemDeploymentsWorkerIntegrationsTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class FlowListResponseItemDeploymentsWorkerIntegrationsTeam(BaseModel):
    id: str

    api_keys: FlowListResponseItemDeploymentsWorkerIntegrationsTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: FlowListResponseItemDeploymentsWorkerIntegrationsTeamUsers

    workers: object


class FlowListResponseItemDeploymentsWorkerIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[FlowListResponseItemDeploymentsWorkerIntegrationsTeam] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class FlowListResponseItemDeploymentsWorkerResourcesDelegateAuxDatabaseResource(BaseModel):
    id: str

    database_name: str = FieldInfo(alias="databaseName")

    delegate_aux_resources: object

    host: str

    password: str

    port: int

    username: str

    connection_string: Optional[str] = FieldInfo(alias="connectionString", default=None)


class FlowListResponseItemDeploymentsWorkerResourcesDelegateAuxRAgResource(BaseModel):
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


class FlowListResponseItemDeploymentsWorkerResources(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    resource_type: object = FieldInfo(alias="resourceType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_database_resource: Optional[
        FlowListResponseItemDeploymentsWorkerResourcesDelegateAuxDatabaseResource
    ] = FieldInfo(alias="delegate_aux_databaseResource", default=None)

    delegate_aux_r_ag_resource: Optional[FlowListResponseItemDeploymentsWorkerResourcesDelegateAuxRAgResource] = (
        FieldInfo(alias="delegate_aux_rAGResource", default=None)
    )


class FlowListResponseItemDeploymentsWorkerTeamAPIKeys(BaseModel):
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


class FlowListResponseItemDeploymentsWorkerTeamIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[object] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class FlowListResponseItemDeploymentsWorkerTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class FlowListResponseItemDeploymentsWorkerTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: FlowListResponseItemDeploymentsWorkerTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class FlowListResponseItemDeploymentsWorkerTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: FlowListResponseItemDeploymentsWorkerTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class FlowListResponseItemDeploymentsWorkerTeam(BaseModel):
    id: str

    api_keys: FlowListResponseItemDeploymentsWorkerTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: FlowListResponseItemDeploymentsWorkerTeamIntegrations

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: FlowListResponseItemDeploymentsWorkerTeamUsers

    workers: object


class FlowListResponseItemDeploymentsWorker(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: object

    flows: object

    integrations: FlowListResponseItemDeploymentsWorkerIntegrations

    name: str

    resources: FlowListResponseItemDeploymentsWorkerResources

    team: FlowListResponseItemDeploymentsWorkerTeam

    team_id: str = FieldInfo(alias="teamId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None

    last_refreshed_at: Optional[datetime] = FieldInfo(alias="lastRefreshedAt", default=None)

    status: Optional[str] = None


class FlowListResponseItemDeploymentsDelegateAuxChatDeployment(BaseModel):
    id: str

    allowed_users: str = FieldInfo(alias="allowedUsers")

    delegate_aux_deployments: object

    api_model_config: object = FieldInfo(alias="modelConfig")

    llm_model: Optional[str] = FieldInfo(alias="llmModel", default=None)

    welcome_message: Optional[str] = FieldInfo(alias="welcomeMessage", default=None)


class FlowListResponseItemDeploymentsDelegateAuxEmailDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    email_template: Optional[str] = FieldInfo(alias="emailTemplate", default=None)

    from_email: Optional[str] = FieldInfo(alias="fromEmail", default=None)

    subject: Optional[str] = None


class FlowListResponseItemDeploymentsDelegateAuxSlackDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    bot_token: Optional[str] = FieldInfo(alias="botToken", default=None)

    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)


class FlowListResponseItemDeploymentsDelegateAuxSMsDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    sms_provider: Optional[str] = FieldInfo(alias="smsProvider", default=None)


class FlowListResponseItemDeploymentsDelegateAuxVoiceDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    voice_id: Optional[str] = FieldInfo(alias="voiceId", default=None)

    voice_provider: Optional[str] = FieldInfo(alias="voiceProvider", default=None)


class FlowListResponseItemDeployments(BaseModel):
    id: str

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    flow: object

    flow_id: str = FieldInfo(alias="flowId")

    history: FlowListResponseItemDeploymentsHistory

    name: str

    status: str

    type: object

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: FlowListResponseItemDeploymentsWorker

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_chat_deployment: Optional[FlowListResponseItemDeploymentsDelegateAuxChatDeployment] = FieldInfo(
        alias="delegate_aux_chatDeployment", default=None
    )

    delegate_aux_email_deployment: Optional[FlowListResponseItemDeploymentsDelegateAuxEmailDeployment] = FieldInfo(
        alias="delegate_aux_emailDeployment", default=None
    )

    delegate_aux_slack_deployment: Optional[FlowListResponseItemDeploymentsDelegateAuxSlackDeployment] = FieldInfo(
        alias="delegate_aux_slackDeployment", default=None
    )

    delegate_aux_s_ms_deployment: Optional[FlowListResponseItemDeploymentsDelegateAuxSMsDeployment] = FieldInfo(
        alias="delegate_aux_sMSDeployment", default=None
    )

    delegate_aux_voice_deployment: Optional[FlowListResponseItemDeploymentsDelegateAuxVoiceDeployment] = FieldInfo(
        alias="delegate_aux_voiceDeployment", default=None
    )


class FlowListResponseItemWorkerDeploymentsHistory(BaseModel):
    id: str

    deployed_at: datetime = FieldInfo(alias="deployedAt")

    deployment: object

    deployment_id: str = FieldInfo(alias="deploymentId")

    flow_version: int = FieldInfo(alias="flowVersion")

    status: str

    metadata: Optional[object] = None


class FlowListResponseItemWorkerDeploymentsDelegateAuxChatDeployment(BaseModel):
    id: str

    allowed_users: str = FieldInfo(alias="allowedUsers")

    delegate_aux_deployments: object

    api_model_config: object = FieldInfo(alias="modelConfig")

    llm_model: Optional[str] = FieldInfo(alias="llmModel", default=None)

    welcome_message: Optional[str] = FieldInfo(alias="welcomeMessage", default=None)


class FlowListResponseItemWorkerDeploymentsDelegateAuxEmailDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    email_template: Optional[str] = FieldInfo(alias="emailTemplate", default=None)

    from_email: Optional[str] = FieldInfo(alias="fromEmail", default=None)

    subject: Optional[str] = None


class FlowListResponseItemWorkerDeploymentsDelegateAuxSlackDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    bot_token: Optional[str] = FieldInfo(alias="botToken", default=None)

    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)


class FlowListResponseItemWorkerDeploymentsDelegateAuxSMsDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    sms_provider: Optional[str] = FieldInfo(alias="smsProvider", default=None)


class FlowListResponseItemWorkerDeploymentsDelegateAuxVoiceDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    voice_id: Optional[str] = FieldInfo(alias="voiceId", default=None)

    voice_provider: Optional[str] = FieldInfo(alias="voiceProvider", default=None)


class FlowListResponseItemWorkerDeployments(BaseModel):
    id: str

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    flow: object

    flow_id: str = FieldInfo(alias="flowId")

    history: FlowListResponseItemWorkerDeploymentsHistory

    name: str

    status: str

    type: object

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_chat_deployment: Optional[FlowListResponseItemWorkerDeploymentsDelegateAuxChatDeployment] = FieldInfo(
        alias="delegate_aux_chatDeployment", default=None
    )

    delegate_aux_email_deployment: Optional[FlowListResponseItemWorkerDeploymentsDelegateAuxEmailDeployment] = (
        FieldInfo(alias="delegate_aux_emailDeployment", default=None)
    )

    delegate_aux_slack_deployment: Optional[FlowListResponseItemWorkerDeploymentsDelegateAuxSlackDeployment] = (
        FieldInfo(alias="delegate_aux_slackDeployment", default=None)
    )

    delegate_aux_s_ms_deployment: Optional[FlowListResponseItemWorkerDeploymentsDelegateAuxSMsDeployment] = FieldInfo(
        alias="delegate_aux_sMSDeployment", default=None
    )

    delegate_aux_voice_deployment: Optional[FlowListResponseItemWorkerDeploymentsDelegateAuxVoiceDeployment] = (
        FieldInfo(alias="delegate_aux_voiceDeployment", default=None)
    )


class FlowListResponseItemWorkerIntegrationsTeamAPIKeys(BaseModel):
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


class FlowListResponseItemWorkerIntegrationsTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class FlowListResponseItemWorkerIntegrationsTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: FlowListResponseItemWorkerIntegrationsTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class FlowListResponseItemWorkerIntegrationsTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: FlowListResponseItemWorkerIntegrationsTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class FlowListResponseItemWorkerIntegrationsTeam(BaseModel):
    id: str

    api_keys: FlowListResponseItemWorkerIntegrationsTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: FlowListResponseItemWorkerIntegrationsTeamUsers

    workers: object


class FlowListResponseItemWorkerIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[FlowListResponseItemWorkerIntegrationsTeam] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class FlowListResponseItemWorkerResourcesDelegateAuxDatabaseResource(BaseModel):
    id: str

    database_name: str = FieldInfo(alias="databaseName")

    delegate_aux_resources: object

    host: str

    password: str

    port: int

    username: str

    connection_string: Optional[str] = FieldInfo(alias="connectionString", default=None)


class FlowListResponseItemWorkerResourcesDelegateAuxRAgResource(BaseModel):
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


class FlowListResponseItemWorkerResources(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    resource_type: object = FieldInfo(alias="resourceType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_database_resource: Optional[FlowListResponseItemWorkerResourcesDelegateAuxDatabaseResource] = (
        FieldInfo(alias="delegate_aux_databaseResource", default=None)
    )

    delegate_aux_r_ag_resource: Optional[FlowListResponseItemWorkerResourcesDelegateAuxRAgResource] = FieldInfo(
        alias="delegate_aux_rAGResource", default=None
    )


class FlowListResponseItemWorkerTeamAPIKeys(BaseModel):
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


class FlowListResponseItemWorkerTeamIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[object] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class FlowListResponseItemWorkerTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class FlowListResponseItemWorkerTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: FlowListResponseItemWorkerTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class FlowListResponseItemWorkerTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: FlowListResponseItemWorkerTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class FlowListResponseItemWorkerTeam(BaseModel):
    id: str

    api_keys: FlowListResponseItemWorkerTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: FlowListResponseItemWorkerTeamIntegrations

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: FlowListResponseItemWorkerTeamUsers

    workers: object


class FlowListResponseItemWorker(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: FlowListResponseItemWorkerDeployments

    flows: object

    integrations: FlowListResponseItemWorkerIntegrations

    name: str

    resources: FlowListResponseItemWorkerResources

    team: FlowListResponseItemWorkerTeam

    team_id: str = FieldInfo(alias="teamId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None

    last_refreshed_at: Optional[datetime] = FieldInfo(alias="lastRefreshedAt", default=None)

    status: Optional[str] = None


class FlowListResponseItem(BaseModel):
    id: str

    code: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: FlowListResponseItemDeployments

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version: int

    worker: FlowListResponseItemWorker

    worker_id: str = FieldInfo(alias="workerId")

    label: Optional[str] = None


FlowListResponse: TypeAlias = List[FlowListResponseItem]
