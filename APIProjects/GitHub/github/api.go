package github

const (
    SearchReposUrl = "https://api.github.com/search/repositories?q="
)

type Repo struct {
    ID int64 `json:"id,omitempty"`
    NodeID string `json:"node_id,omitempty"`
    name string `json:"name,omitempty"`
    FullName string `json:"full_name,omitempty"`
    Private bool `json:"private,omitempty"`
    Owner_ Owner `json:"owner"`
    HTMLURL string `json:"html_url,omitempty"`
    Description string `json:"description,omitempty"`
    Fork bool `json:"fork,omitempty"`
    URL string `json:"url,omitempty"`
    ForksURL string `json:"forks_url,omitempty"`
    KeysURL string `json:"keys_url,omitempty"`
    CollaboratorsURL string `json:"collaborators_url,omitempty"`
    TeamsURL string `json:"team_url,omitempty"`
    HooksURL string `json:"hooks_url,omitempty"`
    IssueEventsURL string `json:"issue_event_url,omitempty"`
    EventsURL string `json:"events_url,omitempty"`
    AssigneesURL string `json:"assignees_url,omitempty"`
    BranchesURL string `json:"branches_url,omitempty"`
    TagsURL string `json:"tags_url,omitempty"`
    BlobsURL string `json:"blobs_url,omitempty"`
    GitTagsURL string `json:"git_tags_url,omitempty"`
    GitRefsURL string `json:"git_regs_url,omitempty"`
    TreesURL string `json:"trees_url,omitempty"`
    StatusesURL string `json:"statuses_url,omitempty"`
    LanguagesURL string `json:"languages_url,omitempty"`
    StargazersURL string `json:"stargazers_url,omitempty"`
    ContributorsURL string `json:"contributors_url,omitempty"`
    SubscribersURL string `json:"subscribers_url,omitempty"`
    SubscriptionURL string `json:"subscription_url,omitempty"`
    CommitsURL string `json:"commits_url,omitempty"`
    GitCommitsURL string `json:"git_commit_url,omitempty"`
    CommentsURL string `json:"comments_url,omitempty"`
    IssueCommentURL string `json:"issue_comment_url,omitempty"`
    ContentsURL string `json:"contents_url,omitempty"`
    CompareURL string `json:"compare_url,omitempty"`
    MergesURL string `json:"merges_url,omitempty"`
    ArchiveURL string `json:"archive_url,omitempty"`
    DownloadsURL string `json:"downloads_url,omitempty"`
    IssuesURL string `json:"issue_url,omitempty"`
    PullsURL string `json:"pulls_url,omitempty"`
    MilestonesURL string `json:"milestones_url,omitempty"`
    NotificationsURL string `json:"notifications_url,omitempty"`
    LabelsURL string `json:"labels_url,omitempty"`
    ReleasesURL string `json:"releases_url,omitempty"`
    DeploymentsURL string `json:"deployment_url,omitempty"`
    CreatedAt string `json:"creared_at,omitempty"`
    UpdatedAt string `json:"updated_at,omitempty"`
    PushedAt string `json:"pushed_at,omitempty"`
    GitURL string `json:"git_url,omitempty"`
    SSHURL string `json:"ssh_url,omitempty"`
    CloneURL string `json:"clone_url,omitempty"`
    SvnURL string `json:"svn_url,omitempty"`
    Homepage *string `json:"homepage,omitempty"`
    Size  int64 `json:"size,omitempty"`
    StargazersCount int64 `json:"stargazers_count,omitempty"`
    WatchersCount int64 `json:"watchers_count,omitempty"`
    Language string `json:"language,omitempty"`
    HasIssues bool `json:"has_issues,omitempty"`
    HasProjects bool `json:"has_projects,omitempty"`
    HasDownloads bool `json:"has_downloads,omitempty"`
    HasWiki bool `json:"has_wiki,omitempty"`
    HasPages bool `json:"has_pages,omitempty"`
    ForksCount int64 `json:"forks_count,omitempty"`
    mirrorURL *string `json:"mirror_url,omitempty"`
    Archived bool `json:"archived,omitempty"`
    Disabled bool `json:"disabled,omitempty"`
    OpenIssuesCount int32 `json:"open_issues_count,omitempty"`
    License License `json:"license,omitempty"`
    Forks int32 `json:"forks,omitempty"`
    OpenIssues int32 `json:"open_issues,omitempty"`
    Watchers int64 `json:"watchers,omitempty"`
    DefaultBranch string `json:"default_branch,omitempty"`
    Score float32 `json:"score,omitempty"`
}

type Owner struct {
    Login string `json:"login,omitempty"`
    ID int64 `json:"id,omitempty"`
    NodeID string `json:"node_id,omitempty"`
    AvatarURL string `json:"avatar_url,omitempty"`
    GravatarID string `json:"gravatar_id,omitempty"`
    URL string `json:"url,omitempty"`
    HTML_URL string `json:"html_url,omitempty"`
    FollowersURL string `json:"followers_url,omitempty"`
    FollowingURL string `json:"following_url,omitempty"`
    GistsURL string `json:"gists_url,omitempty"`
    StarredURL string `json:"starred_url,omitempty"`
    SubscriptionsURL string `json:"subscriptions_url,omitempty"`
    OrganizationsURL string `json:"organizations_url,omitempty"`
    ReposURL string `json:"repos_url,omitempty"`
    EventsURL string `json:"events_url,omitempty"`
    ReceivedEventsURL string `json:"received_events_url,omitempty"`
    Type string `json:"type,omitempty"`
    SiteAdmin bool `json:"site_admin,omitempty"`
}

type License struct {
    Key string `json:"key,omitempty"`
    Name string `json:"name,omitempty"`
    SPDXID string `json:"spdx_id,omitempty"`
    URL *string `json:"url,omitempty"`
    NodeID string `json:"node_id,omitempty"`
}

type RepositoriesSearch struct {
    TotalCount int64 `json:"total_count,omitempty"`
    IncompleteResults bool `json:"incomplete_results,omitempty"`
    Items []Repo `json:"items,omitempty"`
}

/* Example Response
{
  total_count 37210,
  incomplete_results false,
  items [
    {
      id 76954504,
      node_id "MDEwOlJlcG9zaXRvcnk3Njk1NDUwNA==",
      name "react-tetris",
      full_name "chvin/react-tetris",
      private false,
      owner {
        login "chvin",
        id 5383506,
        node_id "MDQ6VXNlcjUzODM1MDY=",
        avatarURL "https://avatars2.githubusercontent.com/u/5383506?v=4",
        gravatar_id "",
        url "https://api.github.com/users/chvin",
        htmlURL "https://github.com/chvin",
        followersURL "https://api.github.com/users/chvin/followers",
        followingURL "https://api.github.com/users/chvin/following{/other_user}",
        gistsURL "https://api.github.com/users/chvin/gists{/gist_id}",
        starredURL "https://api.github.com/users/chvin/starred{/owner}{/repo}",
        subscriptionsURL "https://api.github.com/users/chvin/subscriptions",
        organizationsURL "https://api.github.com/users/chvin/orgs",
        reposURL "https://api.github.com/users/chvin/repos",
        eventsURL "https://api.github.com/users/chvin/events{/privacy}",
        received_eventsURL "https://api.github.com/users/chvin/received_events",
        type "User",
        site_admin false
      },
      htmlURL "https://github.com/chvin/react-tetris",
      description "Use React, Redux, Immutable to code Tetris. 🎮",
      fork false,
      url "https://api.github.com/repos/chvin/react-tetris",
      forksURL "https://api.github.com/repos/chvin/react-tetris/forks",
      keysURL "https://api.github.com/repos/chvin/react-tetris/keys{/key_id}",
      collaboratorsURL "https://api.github.com/repos/chvin/react-tetris/collaborators{/collaborator}",
      teamsURL "https://api.github.com/repos/chvin/react-tetris/teams",
      hooksURL "https://api.github.com/repos/chvin/react-tetris/hooks",
      issue_eventsURL "https://api.github.com/repos/chvin/react-tetris/issues/events{/number}",
      eventsURL "https://api.github.com/repos/chvin/react-tetris/events",
      assigneesURL "https://api.github.com/repos/chvin/react-tetris/assignees{/user}",
      branchesURL "https://api.github.com/repos/chvin/react-tetris/branches{/branch}",
      tagsURL "https://api.github.com/repos/chvin/react-tetris/tags",
      blobsURL "https://api.github.com/repos/chvin/react-tetris/git/blobs{/sha}",
      git_tagsURL "https://api.github.com/repos/chvin/react-tetris/git/tags{/sha}",
      git_refsURL "https://api.github.com/repos/chvin/react-tetris/git/refs{/sha}",
      treesURL "https://api.github.com/repos/chvin/react-tetris/git/trees{/sha}",
      statusesURL "https://api.github.com/repos/chvin/react-tetris/statuses/{sha}",
      languagesURL "https://api.github.com/repos/chvin/react-tetris/languages",
      stargazersURL "https://api.github.com/repos/chvin/react-tetris/stargazers",
      contributorsURL "https://api.github.com/repos/chvin/react-tetris/contributors",
      subscribersURL "https://api.github.com/repos/chvin/react-tetris/subscribers",
      subscriptionURL "https://api.github.com/repos/chvin/react-tetris/subscription",
      commitsURL "https://api.github.com/repos/chvin/react-tetris/commits{/sha}",
      git_commitsURL "https://api.github.com/repos/chvin/react-tetris/git/commits{/sha}",
      commentsURL "https://api.github.com/repos/chvin/react-tetris/comments{/number}",
      issue_commentURL "https://api.github.com/repos/chvin/react-tetris/issues/comments{/number}",
      contentsURL "https://api.github.com/repos/chvin/react-tetris/contents/{+path}",
      compareURL "https://api.github.com/repos/chvin/react-tetris/compare/{base}...{head}",
      mergesURL "https://api.github.com/repos/chvin/react-tetris/merges",
      archiveURL "https://api.github.com/repos/chvin/react-tetris/{archive_format}{/ref}",
      downloadsURL "https://api.github.com/repos/chvin/react-tetris/downloads",
      issuesURL "https://api.github.com/repos/chvin/react-tetris/issues{/number}",
      pullsURL "https://api.github.com/repos/chvin/react-tetris/pulls{/number}",
      milestonesURL "https://api.github.com/repos/chvin/react-tetris/milestones{/number}",
      notificationsURL "https://api.github.com/repos/chvin/react-tetris/notifications{?since,all,participating}",
      labelsURL "https://api.github.com/repos/chvin/react-tetris/labels{/name}",
      releasesURL "https://api.github.com/repos/chvin/react-tetris/releases{/id}",
      deploymentsURL "https://api.github.com/repos/chvin/react-tetris/deployments",
      createdAt "2016-12-20T12:26:11Z",
      updatedAt "2020-11-07T01:49:30Z",
      pushedAt "2020-09-28T13:10:34Z",
      gitURL "git://github.com/chvin/react-tetris.git",
      sshURL "git@github.com:chvin/react-tetris.git",
      cloneURL "https://github.com/chvin/react-tetris.git",
      svnURL "https://github.com/chvin/react-tetris",
      homepage "https://chvin.github.io/react-tetris/?lan=en",
      size 4319,
      stargazers_count 6273,
      watchers_count 6273,
      language "JavaScript",
      has_issues true,
      has_projects true,
      has_downloads true,
      has_wiki true,
      has_pages true,
      forks_count 1188,
      mirrorURL null,
      archived false,
      disabled false,
      open_issues_count 2,
      license null,
      forks 1188,
      open_issues 2,
      watchers 6273,
      default_branch "master",
      score 1.0
    }

*/
