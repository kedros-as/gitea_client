# coding: utf-8

# flake8: noqa

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from gitea_client.api.admin_api import AdminApi
from gitea_client.api.issue_api import IssueApi
from gitea_client.api.miscellaneous_api import MiscellaneousApi
from gitea_client.api.notification_api import NotificationApi
from gitea_client.api.organization_api import OrganizationApi
from gitea_client.api.repository_api import RepositoryApi
from gitea_client.api.user_api import UserApi

# import ApiClient
from gitea_client.api_client import ApiClient
from gitea_client.configuration import Configuration
# import models into sdk package
from gitea_client.models.api_error import APIError
from gitea_client.models.access_token import AccessToken
from gitea_client.models.add_collaborator_option import AddCollaboratorOption
from gitea_client.models.add_time_option import AddTimeOption
from gitea_client.models.annotated_tag import AnnotatedTag
from gitea_client.models.annotated_tag_object import AnnotatedTagObject
from gitea_client.models.attachment import Attachment
from gitea_client.models.branch import Branch
from gitea_client.models.branch_protection import BranchProtection
from gitea_client.models.comment import Comment
from gitea_client.models.commit import Commit
from gitea_client.models.commit_date_options import CommitDateOptions
from gitea_client.models.commit_meta import CommitMeta
from gitea_client.models.commit_user import CommitUser
from gitea_client.models.contents_response import ContentsResponse
from gitea_client.models.create_branch_protection_option import CreateBranchProtectionOption
from gitea_client.models.create_email_option import CreateEmailOption
from gitea_client.models.create_file_options import CreateFileOptions
from gitea_client.models.create_fork_option import CreateForkOption
from gitea_client.models.create_gpg_key_option import CreateGPGKeyOption
from gitea_client.models.create_hook_option import CreateHookOption
from gitea_client.models.create_hook_option_config import CreateHookOptionConfig
from gitea_client.models.create_issue_comment_option import CreateIssueCommentOption
from gitea_client.models.create_issue_option import CreateIssueOption
from gitea_client.models.create_key_option import CreateKeyOption
from gitea_client.models.create_label_option import CreateLabelOption
from gitea_client.models.create_milestone_option import CreateMilestoneOption
from gitea_client.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from gitea_client.models.create_org_option import CreateOrgOption
from gitea_client.models.create_pull_request_option import CreatePullRequestOption
from gitea_client.models.create_release_option import CreateReleaseOption
from gitea_client.models.create_repo_option import CreateRepoOption
from gitea_client.models.create_status_option import CreateStatusOption
from gitea_client.models.create_team_option import CreateTeamOption
from gitea_client.models.create_user_option import CreateUserOption
from gitea_client.models.delete_email_option import DeleteEmailOption
from gitea_client.models.delete_file_options import DeleteFileOptions
from gitea_client.models.deploy_key import DeployKey
from gitea_client.models.edit_attachment_options import EditAttachmentOptions
from gitea_client.models.edit_branch_protection_option import EditBranchProtectionOption
from gitea_client.models.edit_deadline_option import EditDeadlineOption
from gitea_client.models.edit_git_hook_option import EditGitHookOption
from gitea_client.models.edit_hook_option import EditHookOption
from gitea_client.models.edit_issue_comment_option import EditIssueCommentOption
from gitea_client.models.edit_issue_option import EditIssueOption
from gitea_client.models.edit_label_option import EditLabelOption
from gitea_client.models.edit_milestone_option import EditMilestoneOption
from gitea_client.models.edit_org_option import EditOrgOption
from gitea_client.models.edit_pull_request_option import EditPullRequestOption
from gitea_client.models.edit_reaction_option import EditReactionOption
from gitea_client.models.edit_release_option import EditReleaseOption
from gitea_client.models.edit_repo_option import EditRepoOption
from gitea_client.models.edit_team_option import EditTeamOption
from gitea_client.models.edit_user_option import EditUserOption
from gitea_client.models.email import Email
from gitea_client.models.external_tracker import ExternalTracker
from gitea_client.models.external_wiki import ExternalWiki
from gitea_client.models.file_commit_response import FileCommitResponse
from gitea_client.models.file_delete_response import FileDeleteResponse
from gitea_client.models.file_links_response import FileLinksResponse
from gitea_client.models.file_response import FileResponse
from gitea_client.models.gpg_key import GPGKey
from gitea_client.models.gpg_key_email import GPGKeyEmail
from gitea_client.models.git_blob_response import GitBlobResponse
from gitea_client.models.git_entry import GitEntry
from gitea_client.models.git_hook import GitHook
from gitea_client.models.git_object import GitObject
from gitea_client.models.git_tree_response import GitTreeResponse
from gitea_client.models.hook import Hook
from gitea_client.models.identity import Identity
from gitea_client.models.inline_response200 import InlineResponse200
from gitea_client.models.inline_response2001 import InlineResponse2001
from gitea_client.models.internal_tracker import InternalTracker
from gitea_client.models.issue import Issue
from gitea_client.models.issue_deadline import IssueDeadline
from gitea_client.models.issue_labels_option import IssueLabelsOption
from gitea_client.models.label import Label
from gitea_client.models.markdown_option import MarkdownOption
from gitea_client.models.merge_pull_request_option import MergePullRequestOption
from gitea_client.models.migrate_repo_form import MigrateRepoForm
from gitea_client.models.milestone import Milestone
from gitea_client.models.notification_count import NotificationCount
from gitea_client.models.notification_subject import NotificationSubject
from gitea_client.models.notification_thread import NotificationThread
from gitea_client.models.o_auth2_application import OAuth2Application
from gitea_client.models.organization import Organization
from gitea_client.models.pr_branch_info import PRBranchInfo
from gitea_client.models.payload_commit import PayloadCommit
from gitea_client.models.payload_commit_verification import PayloadCommitVerification
from gitea_client.models.payload_user import PayloadUser
from gitea_client.models.permission import Permission
from gitea_client.models.public_key import PublicKey
from gitea_client.models.pull_request import PullRequest
from gitea_client.models.pull_request_meta import PullRequestMeta
from gitea_client.models.reaction import Reaction
from gitea_client.models.reference import Reference
from gitea_client.models.release import Release
from gitea_client.models.repo_commit import RepoCommit
from gitea_client.models.repo_topic_options import RepoTopicOptions
from gitea_client.models.repository import Repository
from gitea_client.models.repository_meta import RepositoryMeta
from gitea_client.models.search_results import SearchResults
from gitea_client.models.server_version import ServerVersion
from gitea_client.models.state_type import StateType
from gitea_client.models.status import Status
from gitea_client.models.status_state import StatusState
from gitea_client.models.stop_watch import StopWatch
from gitea_client.models.tag import Tag
from gitea_client.models.team import Team
from gitea_client.models.time_stamp import TimeStamp
from gitea_client.models.topic_name import TopicName
from gitea_client.models.topic_response import TopicResponse
from gitea_client.models.tracked_time import TrackedTime
from gitea_client.models.transfer_repo_option import TransferRepoOption
from gitea_client.models.update_file_options import UpdateFileOptions
from gitea_client.models.user import User
from gitea_client.models.user_heatmap_data import UserHeatmapData
from gitea_client.models.watch_info import WatchInfo
