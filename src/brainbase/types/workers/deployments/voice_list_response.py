# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "VoiceListResponse",
    "VoiceListResponseItem",
    "VoiceListResponseItemDelegateAuxDeployments",
    "VoiceListResponseItemDelegateAuxDeploymentsFlow",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorker",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrations",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeam",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamAPIKeys",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsers",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUser",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUserIdentities",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerResources",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxDatabaseResource",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxRAgResource",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeam",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamAPIKeys",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamIntegrations",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamUsers",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamUsersUser",
    "VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamUsersUserIdentities",
    "VoiceListResponseItemDelegateAuxDeploymentsHistory",
    "VoiceListResponseItemDelegateAuxDeploymentsWorker",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerFlows",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrations",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeam",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamAPIKeys",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamUsers",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamUsersUser",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamUsersUserIdentities",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerResources",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerResourcesDelegateAuxDatabaseResource",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerResourcesDelegateAuxRAgResource",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerTeam",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamAPIKeys",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamIntegrations",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamUsers",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamUsersUser",
    "VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamUsersUserIdentities",
    "VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxChatDeployment",
    "VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxEmailDeployment",
    "VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxSlackDeployment",
    "VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxSMsDeployment",
]


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamAPIKeys(BaseModel):
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


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeam(BaseModel):
    id: str

    api_keys: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsers

    workers: object


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrationsTeam] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxDatabaseResource(BaseModel):
    id: str

    database_name: str = FieldInfo(alias="databaseName")

    delegate_aux_resources: object

    host: str

    password: str

    port: int

    username: str

    connection_string: Optional[str] = FieldInfo(alias="connectionString", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxRAgResource(BaseModel):
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


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerResources(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    resource_type: object = FieldInfo(alias="resourceType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_database_resource: Optional[
        VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxDatabaseResource
    ] = FieldInfo(alias="delegate_aux_databaseResource", default=None)

    delegate_aux_r_ag_resource: Optional[
        VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxRAgResource
    ] = FieldInfo(alias="delegate_aux_rAGResource", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamAPIKeys(BaseModel):
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


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[object] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeam(BaseModel):
    id: str

    api_keys: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamIntegrations

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeamUsers

    workers: object


class VoiceListResponseItemDelegateAuxDeploymentsFlowWorker(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: object

    flows: object

    integrations: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerIntegrations

    name: str

    resources: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerResources

    team: VoiceListResponseItemDelegateAuxDeploymentsFlowWorkerTeam

    team_id: str = FieldInfo(alias="teamId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None

    last_refreshed_at: Optional[datetime] = FieldInfo(alias="lastRefreshedAt", default=None)

    status: Optional[str] = None


class VoiceListResponseItemDelegateAuxDeploymentsFlow(BaseModel):
    id: str

    code: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version: int

    worker: VoiceListResponseItemDelegateAuxDeploymentsFlowWorker

    worker_id: str = FieldInfo(alias="workerId")

    label: Optional[str] = None


class VoiceListResponseItemDelegateAuxDeploymentsHistory(BaseModel):
    id: str

    deployed_at: datetime = FieldInfo(alias="deployedAt")

    deployment: object

    deployment_id: str = FieldInfo(alias="deploymentId")

    flow_version: int = FieldInfo(alias="flowVersion")

    status: str

    metadata: Optional[object] = None


class VoiceListResponseItemDelegateAuxDeploymentsWorkerFlows(BaseModel):
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


class VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamAPIKeys(BaseModel):
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


class VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeam(BaseModel):
    id: str

    api_keys: VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeamUsers

    workers: object


class VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrationsTeam] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsWorkerResourcesDelegateAuxDatabaseResource(BaseModel):
    id: str

    database_name: str = FieldInfo(alias="databaseName")

    delegate_aux_resources: object

    host: str

    password: str

    port: int

    username: str

    connection_string: Optional[str] = FieldInfo(alias="connectionString", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsWorkerResourcesDelegateAuxRAgResource(BaseModel):
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


class VoiceListResponseItemDelegateAuxDeploymentsWorkerResources(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    resource_type: object = FieldInfo(alias="resourceType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_database_resource: Optional[
        VoiceListResponseItemDelegateAuxDeploymentsWorkerResourcesDelegateAuxDatabaseResource
    ] = FieldInfo(alias="delegate_aux_databaseResource", default=None)

    delegate_aux_r_ag_resource: Optional[
        VoiceListResponseItemDelegateAuxDeploymentsWorkerResourcesDelegateAuxRAgResource
    ] = FieldInfo(alias="delegate_aux_rAGResource", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamAPIKeys(BaseModel):
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


class VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[object] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class VoiceListResponseItemDelegateAuxDeploymentsWorkerTeam(BaseModel):
    id: str

    api_keys: VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamIntegrations

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: VoiceListResponseItemDelegateAuxDeploymentsWorkerTeamUsers

    workers: object


class VoiceListResponseItemDelegateAuxDeploymentsWorker(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: object

    flows: VoiceListResponseItemDelegateAuxDeploymentsWorkerFlows

    integrations: VoiceListResponseItemDelegateAuxDeploymentsWorkerIntegrations

    name: str

    resources: VoiceListResponseItemDelegateAuxDeploymentsWorkerResources

    team: VoiceListResponseItemDelegateAuxDeploymentsWorkerTeam

    team_id: str = FieldInfo(alias="teamId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None

    last_refreshed_at: Optional[datetime] = FieldInfo(alias="lastRefreshedAt", default=None)

    status: Optional[str] = None


class VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxChatDeployment(BaseModel):
    id: str

    allowed_users: str = FieldInfo(alias="allowedUsers")

    delegate_aux_deployments: object

    api_model_config: object = FieldInfo(alias="modelConfig")

    llm_model: Optional[str] = FieldInfo(alias="llmModel", default=None)

    welcome_message: Optional[str] = FieldInfo(alias="welcomeMessage", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxEmailDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    email_template: Optional[str] = FieldInfo(alias="emailTemplate", default=None)

    from_email: Optional[str] = FieldInfo(alias="fromEmail", default=None)

    subject: Optional[str] = None


class VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxSlackDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    bot_token: Optional[str] = FieldInfo(alias="botToken", default=None)

    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)


class VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxSMsDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    sms_provider: Optional[str] = FieldInfo(alias="smsProvider", default=None)


class VoiceListResponseItemDelegateAuxDeployments(BaseModel):
    id: str

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    flow: VoiceListResponseItemDelegateAuxDeploymentsFlow

    flow_id: str = FieldInfo(alias="flowId")

    history: VoiceListResponseItemDelegateAuxDeploymentsHistory

    name: str

    status: str

    type: object

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: VoiceListResponseItemDelegateAuxDeploymentsWorker

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_chat_deployment: Optional[VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxChatDeployment] = (
        FieldInfo(alias="delegate_aux_chatDeployment", default=None)
    )

    delegate_aux_email_deployment: Optional[VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxEmailDeployment] = (
        FieldInfo(alias="delegate_aux_emailDeployment", default=None)
    )

    delegate_aux_slack_deployment: Optional[VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxSlackDeployment] = (
        FieldInfo(alias="delegate_aux_slackDeployment", default=None)
    )

    delegate_aux_s_ms_deployment: Optional[VoiceListResponseItemDelegateAuxDeploymentsDelegateAuxSMsDeployment] = (
        FieldInfo(alias="delegate_aux_sMSDeployment", default=None)
    )

    delegate_aux_voice_deployment: Optional[object] = FieldInfo(alias="delegate_aux_voiceDeployment", default=None)


class VoiceListResponseItem(BaseModel):
    id: str

    delegate_aux_deployments: VoiceListResponseItemDelegateAuxDeployments

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    voice_id: Optional[str] = FieldInfo(alias="voiceId", default=None)

    voice_provider: Optional[str] = FieldInfo(alias="voiceProvider", default=None)


VoiceListResponse: TypeAlias = List[VoiceListResponseItem]
