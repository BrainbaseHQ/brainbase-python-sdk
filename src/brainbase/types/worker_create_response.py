# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "WorkerCreateResponse",
    "Deployments",
    "DeploymentsFlow",
    "DeploymentsHistory",
    "DeploymentsDelegateAuxChatDeployment",
    "DeploymentsDelegateAuxEmailDeployment",
    "DeploymentsDelegateAuxSlackDeployment",
    "DeploymentsDelegateAuxSMsDeployment",
    "DeploymentsDelegateAuxVoiceDeployment",
    "Flows",
    "FlowsDeployments",
    "FlowsDeploymentsHistory",
    "FlowsDeploymentsDelegateAuxChatDeployment",
    "FlowsDeploymentsDelegateAuxEmailDeployment",
    "FlowsDeploymentsDelegateAuxSlackDeployment",
    "FlowsDeploymentsDelegateAuxSMsDeployment",
    "FlowsDeploymentsDelegateAuxVoiceDeployment",
    "Integrations",
    "IntegrationsTeam",
    "IntegrationsTeamAPIKeys",
    "IntegrationsTeamUsers",
    "IntegrationsTeamUsersUser",
    "IntegrationsTeamUsersUserIdentities",
    "Resources",
    "ResourcesDelegateAuxDatabaseResource",
    "ResourcesDelegateAuxRAgResource",
    "Team",
    "TeamAPIKeys",
    "TeamIntegrations",
    "TeamUsers",
    "TeamUsersUser",
    "TeamUsersUserIdentities",
]


class DeploymentsFlow(BaseModel):
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


class DeploymentsHistory(BaseModel):
    id: str

    deployed_at: datetime = FieldInfo(alias="deployedAt")

    deployment: object

    deployment_id: str = FieldInfo(alias="deploymentId")

    flow_version: int = FieldInfo(alias="flowVersion")

    status: str

    metadata: Optional[object] = None


class DeploymentsDelegateAuxChatDeployment(BaseModel):
    id: str

    allowed_users: str = FieldInfo(alias="allowedUsers")

    delegate_aux_deployments: object

    api_model_config: object = FieldInfo(alias="modelConfig")

    llm_model: Optional[str] = FieldInfo(alias="llmModel", default=None)

    welcome_message: Optional[str] = FieldInfo(alias="welcomeMessage", default=None)


class DeploymentsDelegateAuxEmailDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    email_template: Optional[str] = FieldInfo(alias="emailTemplate", default=None)

    from_email: Optional[str] = FieldInfo(alias="fromEmail", default=None)

    subject: Optional[str] = None


class DeploymentsDelegateAuxSlackDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    bot_token: Optional[str] = FieldInfo(alias="botToken", default=None)

    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)


class DeploymentsDelegateAuxSMsDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    sms_provider: Optional[str] = FieldInfo(alias="smsProvider", default=None)


class DeploymentsDelegateAuxVoiceDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    voice_id: Optional[str] = FieldInfo(alias="voiceId", default=None)

    voice_provider: Optional[str] = FieldInfo(alias="voiceProvider", default=None)


class Deployments(BaseModel):
    id: str

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    flow: DeploymentsFlow

    flow_id: str = FieldInfo(alias="flowId")

    history: DeploymentsHistory

    name: str

    status: str

    type: object

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_chat_deployment: Optional[DeploymentsDelegateAuxChatDeployment] = FieldInfo(
        alias="delegate_aux_chatDeployment", default=None
    )

    delegate_aux_email_deployment: Optional[DeploymentsDelegateAuxEmailDeployment] = FieldInfo(
        alias="delegate_aux_emailDeployment", default=None
    )

    delegate_aux_slack_deployment: Optional[DeploymentsDelegateAuxSlackDeployment] = FieldInfo(
        alias="delegate_aux_slackDeployment", default=None
    )

    delegate_aux_s_ms_deployment: Optional[DeploymentsDelegateAuxSMsDeployment] = FieldInfo(
        alias="delegate_aux_sMSDeployment", default=None
    )

    delegate_aux_voice_deployment: Optional[DeploymentsDelegateAuxVoiceDeployment] = FieldInfo(
        alias="delegate_aux_voiceDeployment", default=None
    )


class FlowsDeploymentsHistory(BaseModel):
    id: str

    deployed_at: datetime = FieldInfo(alias="deployedAt")

    deployment: object

    deployment_id: str = FieldInfo(alias="deploymentId")

    flow_version: int = FieldInfo(alias="flowVersion")

    status: str

    metadata: Optional[object] = None


class FlowsDeploymentsDelegateAuxChatDeployment(BaseModel):
    id: str

    allowed_users: str = FieldInfo(alias="allowedUsers")

    delegate_aux_deployments: object

    api_model_config: object = FieldInfo(alias="modelConfig")

    llm_model: Optional[str] = FieldInfo(alias="llmModel", default=None)

    welcome_message: Optional[str] = FieldInfo(alias="welcomeMessage", default=None)


class FlowsDeploymentsDelegateAuxEmailDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    email_template: Optional[str] = FieldInfo(alias="emailTemplate", default=None)

    from_email: Optional[str] = FieldInfo(alias="fromEmail", default=None)

    subject: Optional[str] = None


class FlowsDeploymentsDelegateAuxSlackDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    bot_token: Optional[str] = FieldInfo(alias="botToken", default=None)

    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)


class FlowsDeploymentsDelegateAuxSMsDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    sms_provider: Optional[str] = FieldInfo(alias="smsProvider", default=None)


class FlowsDeploymentsDelegateAuxVoiceDeployment(BaseModel):
    id: str

    delegate_aux_deployments: object

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    voice_id: Optional[str] = FieldInfo(alias="voiceId", default=None)

    voice_provider: Optional[str] = FieldInfo(alias="voiceProvider", default=None)


class FlowsDeployments(BaseModel):
    id: str

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    flow: object

    flow_id: str = FieldInfo(alias="flowId")

    history: FlowsDeploymentsHistory

    name: str

    status: str

    type: object

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_chat_deployment: Optional[FlowsDeploymentsDelegateAuxChatDeployment] = FieldInfo(
        alias="delegate_aux_chatDeployment", default=None
    )

    delegate_aux_email_deployment: Optional[FlowsDeploymentsDelegateAuxEmailDeployment] = FieldInfo(
        alias="delegate_aux_emailDeployment", default=None
    )

    delegate_aux_slack_deployment: Optional[FlowsDeploymentsDelegateAuxSlackDeployment] = FieldInfo(
        alias="delegate_aux_slackDeployment", default=None
    )

    delegate_aux_s_ms_deployment: Optional[FlowsDeploymentsDelegateAuxSMsDeployment] = FieldInfo(
        alias="delegate_aux_sMSDeployment", default=None
    )

    delegate_aux_voice_deployment: Optional[FlowsDeploymentsDelegateAuxVoiceDeployment] = FieldInfo(
        alias="delegate_aux_voiceDeployment", default=None
    )


class Flows(BaseModel):
    id: str

    code: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: FlowsDeployments

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    version: int

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    label: Optional[str] = None


class IntegrationsTeamAPIKeys(BaseModel):
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


class IntegrationsTeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class IntegrationsTeamUsersUser(BaseModel):
    id: str

    email: str

    identities: IntegrationsTeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class IntegrationsTeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: IntegrationsTeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class IntegrationsTeam(BaseModel):
    id: str

    api_keys: IntegrationsTeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: object

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: IntegrationsTeamUsers

    workers: object


class Integrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[IntegrationsTeam] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class ResourcesDelegateAuxDatabaseResource(BaseModel):
    id: str

    database_name: str = FieldInfo(alias="databaseName")

    delegate_aux_resources: object

    host: str

    password: str

    port: int

    username: str

    connection_string: Optional[str] = FieldInfo(alias="connectionString", default=None)


class ResourcesDelegateAuxRAgResource(BaseModel):
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


class Resources(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    resource_type: object = FieldInfo(alias="resourceType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    worker: object

    worker_id: str = FieldInfo(alias="workerId")

    delegate_aux_database_resource: Optional[ResourcesDelegateAuxDatabaseResource] = FieldInfo(
        alias="delegate_aux_databaseResource", default=None
    )

    delegate_aux_r_ag_resource: Optional[ResourcesDelegateAuxRAgResource] = FieldInfo(
        alias="delegate_aux_rAGResource", default=None
    )


class TeamAPIKeys(BaseModel):
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


class TeamIntegrations(BaseModel):
    id: str

    app_type: str = FieldInfo(alias="appType")

    config: object

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    team: Optional[object] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    worker: Optional[object] = None

    worker_id: Optional[str] = FieldInfo(alias="workerId", default=None)


class TeamUsersUserIdentities(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")

    provider: str

    provider_id: str = FieldInfo(alias="providerId")

    user: object

    user_id: str = FieldInfo(alias="userId")

    metadata: Optional[object] = None


class TeamUsersUser(BaseModel):
    id: str

    email: str

    identities: TeamUsersUserIdentities

    teams: object

    email_verified: Optional[datetime] = FieldInfo(alias="emailVerified", default=None)

    hashed_password: Optional[str] = FieldInfo(alias="hashedPassword", default=None)

    image: Optional[str] = None

    metadata: Optional[object] = None

    verification_token: Optional[str] = FieldInfo(alias="verificationToken", default=None)

    verification_token_expires: Optional[datetime] = FieldInfo(alias="verificationTokenExpires", default=None)


class TeamUsers(BaseModel):
    permissions: str

    team: object

    team_id: str = FieldInfo(alias="teamId")

    user: TeamUsersUser

    user_id: str = FieldInfo(alias="userId")


class Team(BaseModel):
    id: str

    api_keys: TeamAPIKeys = FieldInfo(alias="apiKeys")

    created_at: datetime = FieldInfo(alias="createdAt")

    integrations: TeamIntegrations

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    users: TeamUsers

    workers: object


class WorkerCreateResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    deployments: Deployments

    flows: Flows

    integrations: Integrations

    name: str

    resources: Resources

    team: Team

    team_id: str = FieldInfo(alias="teamId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None

    last_refreshed_at: Optional[datetime] = FieldInfo(alias="lastRefreshedAt", default=None)

    status: Optional[str] = None
