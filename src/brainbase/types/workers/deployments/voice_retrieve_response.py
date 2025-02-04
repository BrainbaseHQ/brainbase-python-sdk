# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "VoiceRetrieveResponse",
    "DelegateAuxDeployments",
    "DelegateAuxDeploymentsFlow",
    "DelegateAuxDeploymentsFlowWorker",
    "DelegateAuxDeploymentsFlowWorkerIntegrations",
    "DelegateAuxDeploymentsFlowWorkerIntegrationsTeam",
    "DelegateAuxDeploymentsFlowWorkerIntegrationsTeamAPIKeys",
    "DelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsers",
    "DelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUser",
    "DelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUserIdentities",
    "DelegateAuxDeploymentsFlowWorkerResources",
    "DelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxDatabaseResource",
    "DelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxRAgResource",
    "DelegateAuxDeploymentsFlowWorkerTeam",
    "DelegateAuxDeploymentsFlowWorkerTeamAPIKeys",
    "DelegateAuxDeploymentsFlowWorkerTeamIntegrations",
    "DelegateAuxDeploymentsFlowWorkerTeamUsers",
    "DelegateAuxDeploymentsFlowWorkerTeamUsersUser",
    "DelegateAuxDeploymentsFlowWorkerTeamUsersUserIdentities",
    "DelegateAuxDeploymentsHistory",
    "DelegateAuxDeploymentsWorker",
    "DelegateAuxDeploymentsWorkerFlows",
    "DelegateAuxDeploymentsWorkerIntegrations",
    "DelegateAuxDeploymentsWorkerIntegrationsTeam",
    "DelegateAuxDeploymentsWorkerIntegrationsTeamAPIKeys",
    "DelegateAuxDeploymentsWorkerIntegrationsTeamUsers",
    "DelegateAuxDeploymentsWorkerIntegrationsTeamUsersUser",
    "DelegateAuxDeploymentsWorkerIntegrationsTeamUsersUserIdentities",
    "DelegateAuxDeploymentsWorkerResources",
    "DelegateAuxDeploymentsWorkerResourcesDelegateAuxDatabaseResource",
    "DelegateAuxDeploymentsWorkerResourcesDelegateAuxRAgResource",
    "DelegateAuxDeploymentsWorkerTeam",
    "DelegateAuxDeploymentsWorkerTeamAPIKeys",
    "DelegateAuxDeploymentsWorkerTeamIntegrations",
    "DelegateAuxDeploymentsWorkerTeamUsers",
    "DelegateAuxDeploymentsWorkerTeamUsersUser",
    "DelegateAuxDeploymentsWorkerTeamUsersUserIdentities",
    "DelegateAuxDeploymentsDelegateAuxChatDeployment",
    "DelegateAuxDeploymentsDelegateAuxEmailDeployment",
    "DelegateAuxDeploymentsDelegateAuxSlackDeployment",
    "DelegateAuxDeploymentsDelegateAuxSMsDeployment",
]


class DelegateAuxDeploymentsFlowWorkerIntegrationsTeamAPIKeys(BaseModel):
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


class DelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class DelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: DelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class DelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: DelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class DelegateAuxDeploymentsFlowWorkerIntegrationsTeam(BaseModel):
    id: str

    api_keys: DelegateAuxDeploymentsFlowWorkerIntegrationsTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: DelegateAuxDeploymentsFlowWorkerIntegrationsTeamUsers

    workers: object


class DelegateAuxDeploymentsFlowWorkerIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[DelegateAuxDeploymentsFlowWorkerIntegrationsTeam] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class DelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxDatabaseResource(BaseModel):
    id: str

    database_name: str = FieldInfo(alias="databaseName")

    delegate_aux_resources: object

    host: str

    password: str

    port: int

    username: str

    connection_string: Optional[str] = FieldInfo(alias="connectionString", default=None)


class DelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxRAgResource(BaseModel):
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


class DelegateAuxDeploymentsFlowWorkerResources(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    resource_type: object = FieldInfo(alias="resourceType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_database_resource: Optional[DelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxDatabaseResource] = (
        FieldInfo(alias="delegate_aux_databaseResource", default=None)
    )

    delegate_aux_r_ag_resource: Optional[DelegateAuxDeploymentsFlowWorkerResourcesDelegateAuxRAgResource] = FieldInfo(
        alias="delegate_aux_rAGResource", default=None
    )


class DelegateAuxDeploymentsFlowWorkerTeamAPIKeys(BaseModel):
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


class DelegateAuxDeploymentsFlowWorkerTeamIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[object] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class DelegateAuxDeploymentsFlowWorkerTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class DelegateAuxDeploymentsFlowWorkerTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: DelegateAuxDeploymentsFlowWorkerTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class DelegateAuxDeploymentsFlowWorkerTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: DelegateAuxDeploymentsFlowWorkerTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class DelegateAuxDeploymentsFlowWorkerTeam(BaseModel):
    id: str

    api_keys: DelegateAuxDeploymentsFlowWorkerTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: DelegateAuxDeploymentsFlowWorkerTeamIntegrations

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: DelegateAuxDeploymentsFlowWorkerTeamUsers

    workers: object


class DelegateAuxDeploymentsFlowWorker(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: object

    flows: object

    integrations: DelegateAuxDeploymentsFlowWorkerIntegrations

    name: str

    resources: DelegateAuxDeploymentsFlowWorkerResources

    team: DelegateAuxDeploymentsFlowWorkerTeam

    team_id: str = FieldInfo(alias="teamId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None

    last_refreshed_at: Optional[datetime] = FieldInfo(alias="lastRefreshedAt", default=None)

    status: Optional[str] = None


class DelegateAuxDeploymentsFlow(BaseModel):
    id: str

    code: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version: int

    worker: DelegateAuxDeploymentsFlowWorker

    worker_id: str = FieldInfo(alias="workerId")

    label: Optional[str] = None


class DelegateAuxDeploymentsHistory(BaseModel):
    id: str

    deployed_at: datetime = FieldInfo(alias="deployedAt")

    deployment: object

    deployment_id: str = FieldInfo(alias="deploymentId")

    flow_version: int = FieldInfo(alias="flowVersion")

    status: str

    metadata: Optional[object] = None


class DelegateAuxDeploymentsWorkerFlows(BaseModel):
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


class DelegateAuxDeploymentsWorkerIntegrationsTeamAPIKeys(BaseModel):
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


class DelegateAuxDeploymentsWorkerIntegrationsTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class DelegateAuxDeploymentsWorkerIntegrationsTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: DelegateAuxDeploymentsWorkerIntegrationsTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class DelegateAuxDeploymentsWorkerIntegrationsTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: DelegateAuxDeploymentsWorkerIntegrationsTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class DelegateAuxDeploymentsWorkerIntegrationsTeam(BaseModel):
    id: str

    api_keys: DelegateAuxDeploymentsWorkerIntegrationsTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: DelegateAuxDeploymentsWorkerIntegrationsTeamUsers

    workers: object


class DelegateAuxDeploymentsWorkerIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[DelegateAuxDeploymentsWorkerIntegrationsTeam] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class DelegateAuxDeploymentsWorkerResourcesDelegateAuxDatabaseResource(BaseModel):
    id: str

    database_name: str = FieldInfo(alias="databaseName")

    delegate_aux_resources: object

    host: str

    password: str

    port: int

    username: str

    connection_string: Optional[str] = FieldInfo(alias="connectionString", default=None)


class DelegateAuxDeploymentsWorkerResourcesDelegateAuxRAgResource(BaseModel):
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


class DelegateAuxDeploymentsWorkerResources(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    resource_type: object = FieldInfo(alias="resourceType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_database_resource: Optional[DelegateAuxDeploymentsWorkerResourcesDelegateAuxDatabaseResource] = (
        FieldInfo(alias="delegate_aux_databaseResource", default=None)
    )

    delegate_aux_r_ag_resource: Optional[DelegateAuxDeploymentsWorkerResourcesDelegateAuxRAgResource] = FieldInfo(
        alias="delegate_aux_rAGResource", default=None
    )


class DelegateAuxDeploymentsWorkerTeamAPIKeys(BaseModel):
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


class DelegateAuxDeploymentsWorkerTeamIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[object] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class DelegateAuxDeploymentsWorkerTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class DelegateAuxDeploymentsWorkerTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: DelegateAuxDeploymentsWorkerTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class DelegateAuxDeploymentsWorkerTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: DelegateAuxDeploymentsWorkerTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class DelegateAuxDeploymentsWorkerTeam(BaseModel):
    id: str

    api_keys: DelegateAuxDeploymentsWorkerTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: DelegateAuxDeploymentsWorkerTeamIntegrations

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: DelegateAuxDeploymentsWorkerTeamUsers

    workers: object


class DelegateAuxDeploymentsWorker(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: object

    flows: DelegateAuxDeploymentsWorkerFlows

    integrations: DelegateAuxDeploymentsWorkerIntegrations

    name: str

    resources: DelegateAuxDeploymentsWorkerResources

    team: DelegateAuxDeploymentsWorkerTeam

    team_id: str = FieldInfo(alias="teamId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None

    last_refreshed_at: Optional[datetime] = FieldInfo(alias="lastRefreshedAt", default=None)

    status: Optional[str] = None


class DelegateAuxDeploymentsDelegateAuxChatDeployment(BaseModel):
    id: str

    allowed_users: str = FieldInfo(alias="allowedUsers")

    delegate_aux_deployments: object

    api_model_config: object = FieldInfo(alias="modelConfig")

    llm_model: Optional[str] = FieldInfo(alias="llmModel", default=None)

    welcome_message: Optional[str] = FieldInfo(alias="welcomeMessage", default=None)


class DelegateAuxDeploymentsDelegateAuxEmailDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    email_template: Optional[str] = FieldInfo(alias="emailTemplate", default=None)

    from_email: Optional[str] = FieldInfo(alias="fromEmail", default=None)

    subject: Optional[str] = None


class DelegateAuxDeploymentsDelegateAuxSlackDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    bot_token: Optional[str] = FieldInfo(alias="botToken", default=None)

    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)


class DelegateAuxDeploymentsDelegateAuxSMsDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    sms_provider: Optional[str] = FieldInfo(alias="smsProvider", default=None)


class DelegateAuxDeployments(BaseModel):
    id: str

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    flow: DelegateAuxDeploymentsFlow

    flow_id: str = FieldInfo(alias="flowId")

    history: DelegateAuxDeploymentsHistory

    name: str

    status: str

    type: object

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: DelegateAuxDeploymentsWorker

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_chat_deployment: Optional[DelegateAuxDeploymentsDelegateAuxChatDeployment] = FieldInfo(
        alias="delegate_aux_chatDeployment", default=None
    )

    delegate_aux_email_deployment: Optional[DelegateAuxDeploymentsDelegateAuxEmailDeployment] = FieldInfo(
        alias="delegate_aux_emailDeployment", default=None
    )

    delegate_aux_slack_deployment: Optional[DelegateAuxDeploymentsDelegateAuxSlackDeployment] = FieldInfo(
        alias="delegate_aux_slackDeployment", default=None
    )

    delegate_aux_s_ms_deployment: Optional[DelegateAuxDeploymentsDelegateAuxSMsDeployment] = FieldInfo(
        alias="delegate_aux_sMSDeployment", default=None
    )

    delegate_aux_voice_deployment: Optional[object] = FieldInfo(alias="delegate_aux_voiceDeployment", default=None)


class VoiceRetrieveResponse(BaseModel):
    id: str

    delegate_aux_deployments: DelegateAuxDeployments

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    voice_id: Optional[str] = FieldInfo(alias="voiceId", default=None)

    voice_provider: Optional[str] = FieldInfo(alias="voiceProvider", default=None)
